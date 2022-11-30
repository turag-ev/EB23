from EB23_Enums import State


class ActuatorState:
    """
    Class to define the operating state of actuators.
    """

    actuator_state: dict

    def __init__(self, actuators: list) -> None:
        for actuator in actuators:
            self.actuator_state[actuator] = State.FREE

    def getActuatorState(self) -> dict:
        """
        Get state of all actuators.

        Returns:
            dict (Actuator: ActuatorState): dictionary containing all actuator states with actuator objects as keys
        """
        return self.actuator_state

    def check_availability(self, requested_actuators: list) -> bool:
        for actuator in requested_actuators:
            if self.actuator_state[actuator] != State.FREE:
                return False
        return True

    def request_actuators(self, requested_actuators: list) -> bool:
        if not self.check_availability(requested_actuators):
            return False

        else:
            for actuator in requested_actuators:
                self.actuator_state[actuator] = State.OCCUPIED

            return True

    def free_actuators(self, actuators: list):
        for actuator in actuators:
            self.actuator_state[actuator] = State.FREE
