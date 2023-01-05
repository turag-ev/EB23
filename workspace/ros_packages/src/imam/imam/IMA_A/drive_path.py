from im_actions.action import DrivePath as DrivePathAction
from EB23_Enums import Actuator
from IMA_Interface import IMA
from turag_lmc import DriveSplineTask, Pose
from rclpy.node import Node
from time import sleep


class DrivePath(IMA):
    def __init__(self) -> None:
        super().__init__()

    def registerIMA() -> dict:

        properties = {}
        properties["IMA"] = DrivePath
        properties["action_type"] = DrivePathAction
        properties["required_actuators"] = [Actuator.LMC]

        register = {}
        register["DriveToPath"] = properties

        return register

    def execute(self, imam: Node, goal_handle, **kwargs) -> True:
        path: list = goal_handle.request.path

        for spline in path:
            spline_poses = [
                Pose(x=pose.x, y=pose.y, angle=pose.angle) for pose in spline.poses
            ]
            spline_task = DriveSplineTask(
                pose_list=spline_poses,
                drive_flags=spline.drive_flag,
                drive_ramp=spline.ramp,
            )
            imam.lmc.issueDriveTask(spline_task)

            # TODO wait until drive task is finished

        return True
