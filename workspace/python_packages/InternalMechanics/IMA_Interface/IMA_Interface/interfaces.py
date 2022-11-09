from abc import ABC, abstractmethod

from EB23_Enums import Actuator


class MajorAction(ABC):
    """
    Interface for major Internal Mechanics Actions.

    Can be accessed by GamePlanning.
    """

    used_actuators = []

    def getActuators(self):
        """
        Get used actuators.

        Returns:
            list[Actuator]: used actuators
        """
        return self.used_actuators

    @abstractmethod
    def prepare(self, imam: object, **kw_actuators):
        pass

    @abstractmethod
    def execute(self, imam: object, **kw_actuators):
        pass

    @abstractmethod
    def postProcess(self, imam: object, **kw_actuators):
        pass


class MinorAction(ABC):
    """
    Interface for minor Internal Mechanics Actions.

    Cannot be accessed by GamePlanning.
    """

    used_actuators = []

    def getActuators(self):
        """
        Get used actuators.

        Returns:
            list[Actuator]: used actuators
        """
        return self.used_actuators

    @abstractmethod
    def execute(self, imam: object, **kw_actuators):
        pass
