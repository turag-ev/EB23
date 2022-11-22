from dataclasses import dataclass
from EB23_Enums import ActuatorState


@dataclass
class ActuatorStatus:
    """
    Class to define the operating state of actuators.
    """

    actuator_status: dict

    def __init__(self, actuators: list()) -> None:
        for actuator in actuators:
            self.actuator_status[actuator] = ActuatorState.FREE

    def setActuatorState(self, actuator, state: ActuatorState) -> None:
        """
        Set actuator status.

        Args:
            actuator (Actuator): reference to actuator object
            state (ActuatorState):
        """
        self.actuator_status[actuator] = state

    def getActuatorState(self, actuator) -> ActuatorState:
        """
        Get state of provided actuator.

        Args:
            actuator (Actuator): reference to actuator object

        Returns:
            ActuatorState: state of actuator, FREE or OCCUPIED
        """
        return self.actuator_status[actuator]

    def getActuatorStateAll(self) -> dict:
        """
        Get state of all actuators.

        Returns:
            dict (Actuator: ActuatorState): dictionary containing all actuator states with actuator objects as keys
        """
        return self.actuator_status

    def getActuatorStateAllString(self) -> dict:
        """
        Get state of actuators with name of actuators as keys.
        Could be usefull if published.

        Returns:
            dict (str: ActuatorState): dictionary containing all actuator states with actuator names as keys
        """
        actuator_status_string: dict
        for actuator, state in self.actuator_status.items():
            actuator_status_string[actuator.name] = state

        return actuator_status_string
