import rclpy
import asyncio
from im_actions.action import Trigger
from rclpy.action import ActionServer, GoalResponse, CancelResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.timer import Timer
from time import sleep
import collections

import IMA_Interface
from .IMA_A import PickUp, Store, BuildCake, Drop
from asyncio import run
import sys
import inspect
import threading


class Servers:
    def __init__(self, imam):
        self.imam = imam
        self.actions = []  # [PickUp, Store, BuildCake, Drop]
        for _, cls in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(cls) and issubclass(cls, IMA_Interface.IMA):
                self.actions.append(cls)

        self._goal_queue = collections.deque()
        self._goal_queue_lock = threading.Lock()

        self.action_servers = {}

        for action in self.actions:
            register = action.registerIMA()

            for name, properties in register.items():
                if name in self.action_servers.keys():
                    self.imam.get_logger().warn(
                        f"Action Server for {name} already exists. Cannot create more than one server for the same IMA"
                    )
                    raise KeyError(
                        f"Action Server for {name} already exists. Cannot create more than one server for the same IMA"
                    )
                server = ActionServer(
                    node=self.imam,
                    action_type=properties["action_type"],
                    action_name=f"IMA/{name}",
                    goal_callback=lambda goal_request, properties=properties: run(
                        self.goal_callback(goal_request, properties)
                    ),
                    handle_accepted_callback=lambda goal_handle, properties=properties: run(
                        self.handle_accepted_callback(goal_handle, properties)
                    ),
                    execute_callback=lambda goal_handle, properties=properties: run(
                        self.common_callback(goal_handle, properties)
                    ),
                    cancel_callback=self.cancel_callback,
                    callback_group=ReentrantCallbackGroup(),
                )

                self.imam.log_info(f"Registered Action Server for {name}.")
                self.action_servers[name] = server

        self._timer = self.imam.create_timer(0.2, self.execute_queued_goal)

    async def common_callback(self, goal_handle, properties: dict):
        """
        Executes IMAs.

        Args:
            goal_handle (goal_handle): action goal handle
            properties (dict): properties of IMA

        Returns:
            result: action result
        """
        action = properties["IMA"]()
        success = action.execute(self.imam, goal_handle)
        action_type = properties["action_type"]
        result = action_type.Result()

        if success:
            goal_handle.succeed()
            result.result = "Done"
        else:
            goal_handle.canceled()

        self.imam.actuator_state.free_actuators(properties["required_actuators"])

        return result

    async def handle_accepted_callback(self, goal_handle, properties: dict):
        """
        Adds accepted goals to action queue.

        Args:
            goal_handle (goal_handle): _action goal handle
            properties (dict): properties of IMA
        """
        name = properties["IMA"]
        if goal_handle.request.queue_goal:
            self._goal_queue.append((goal_handle, properties["required_actuators"]))
        else:
            self._goal_queue.appendleft((goal_handle, properties["required_actuators"]))
            
        self.imam.log_info(f"Added {name} to action queue.")

    async def goal_callback(self, goal_request, properties: dict):
        """
        Rejects goal if it is not queueable and their actuators are not available.

        Args:
            goal_request (goal_request): action goal request
            properties (dict): properties of IMA

        Returns:
            GoalResponse: ACCEPT if goal accepted, REJECT if rejected
        """
        name = properties["IMA"]

        if goal_request.queue_goal or self.imam.actuator_state.check_availability(
            properties["required_actuators"]
        ):
            return GoalResponse.ACCEPT
        else:
            self.imam.log_info(
                f"Action {name} rejected. Required actuators are not available."
            )
            return GoalResponse.REJECT

    def cancel_callback(self, goal_handle):
        """
        Cancels action on request.
        In order to actually cancel actions IMAs need to regularly check whether
        goal_handle.is_cancel_request == True.
        In case of it being true, cancel ongoing subactions and return False.

        Args:
            goal_handle (goal_handle): action goal handle

        Returns:
            CancelRepsonse: enum telling whether request was accepted or rejected
        """
        self.imam.log_info(f"Cancelling Action.")
        return CancelResponse.ACCEPT

    def execute_queued_goal(self):
        """
        Checks goal queue for actions that could be executed.
        If their motors are available, they are executed.
        """
        for action in self._goal_queue:
            gh = action[0]
            actuators = action[1]

            if self.imam.actuator_state.check_availability(actuators):
                self.imam.actuator_state.reserve_actuators(actuators)
                self._goal_queue.remove(action)
                gh.execute()
