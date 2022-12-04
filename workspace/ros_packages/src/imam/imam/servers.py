import rclpy
import asyncio
from im_actions.action import Trigger
from rclpy.action import ActionServer, GoalResponse
from rclpy.callback_groups import ReentrantCallbackGroup
from rclpy.timer import Timer
from time import sleep
import collections

import IMA_Interface
from .IMA_A import PickUp, Store, BuildCake, Drop
from asyncio import run
import sys
import inspect


class Servers:
    def __init__(self, imam):
        self.imam = imam
        self.actions = []  # [PickUp, Store, BuildCake, Drop]
        for _, cls in inspect.getmembers(sys.modules[__name__]):
            if inspect.isclass(cls) and issubclass(cls, IMA_Interface.IMA):
                self.actions.append(cls)

        self._goal_queue = collections.deque()

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
                    callback_group=ReentrantCallbackGroup(),
                )

                self.imam.log_info(f"Registered Action Server for {name}.")
                self.action_servers[name] = server

                self._timer = self.imam.create_timer(0.2, self.execute_queued_goal)

    async def common_callback(self, goal_handle, properties):
        action = properties["IMA"]()
        action.execute(self.imam, goal_handle)
        goal_handle.succeed()
        action_type = properties["action_type"]
        result = action_type.Result()
        result.result = "Done"
        self.imam.actuator_state.free_actuators(properties["required_actuators"])

        return result

    async def handle_accepted_callback(self, goal_handle, properties):
        name = properties["IMA"]
        self._goal_queue.append((goal_handle, properties["required_actuators"]))
        self.imam.log_info(f"Added {name} to action queue.")

    async def goal_callback(self, goal_request, properties):
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

    def execute_queued_goal(self):
        for action in self._goal_queue:
            gh = action[0]
            actuators = action[1]

            if self.imam.actuator_state.check_availability(actuators):
                self.imam.actuator_state.reserve_actuators(actuators)
                self._goal_queue.remove(action)
                gh.execute()
