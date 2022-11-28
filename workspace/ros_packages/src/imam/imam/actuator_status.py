from EB23_Enums import ActuatorState


class ActuatorStatus:
    """
    Class to define the operating state of actuators.
    """

    actuator_status: dict

    def __init__(self, actuators: list()) -> None:
        for actuator in actuators:
            self.actuator_status[actuator] = ActuatorState.FREE

    def getActuatorState(self) -> dict:
        """
        Get state of all actuators.

        Returns:
            dict (Actuator: ActuatorState): dictionary containing all actuator states with actuator objects as keys
        """
        return self.actuator_status

    def check_availability():
        pass

    def request_actuators():
        pass
