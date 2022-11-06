from abc import ABC, abstractmethod
from EB23_Enums import Actuator


class IMA_Interface(ABC):
    """
    Interface for Internal Mechanics Actions.
    """

    used_actuators: list[Actuator]

    def getActuators(self) -> list[Actuator]:
        """
        Get used actuators.

        Returns:
            list[Actuator]: used actuators
        """
        return self.used_actuators

    @abstractmethod
    def prepare(self, imam, **kw_actuators):
        pass

    @abstractmethod
    def execute(self, imam, **kw_actuators):
        pass

    @abstractmethod
    def postProcess(self, imam, **kw_actuators):
        pass
