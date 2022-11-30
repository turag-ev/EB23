import rclpy
import asyncio
from im_actions.action import Trigger
from rclpy.action import ActionServer
from rclpy.callback_groups import ReentrantCallbackGroup
from time import sleep

from .IMA_A import PickUp, Store, BuildCake, Drop
from asyncio import run


class Servers:
    def __init__(self, imam):
        self.imam = imam
        self.actions = [PickUp, Store, BuildCake, Drop]
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
                print(properties)
                server = ActionServer(
                    node=self.imam,
                    action_type=properties["action_type"],
                    action_name=f"IMA/{name}",
                    execute_callback=lambda goal_handle: run(
                        self.common_callback(goal_handle, properties)
                    ),
                    callback_group=ReentrantCallbackGroup(),
                )

            self.action_servers[name] = server

    async def common_callback(self, goal_handle, properties):
        self.imam.get_logger().info(str(properties))
        actuators_available = True

        if actuators_available:
            action = properties["IMA"]()
            action.execute(self.imam, goal_handle)
            goal_handle.succeed()
            action_type = properties["action_type"]
            result = action_type.Result()
            result.result = "Done"

        return result
