from abc import ABC, abstractmethod

from EB23_Enums import Actuator


class IMA(ABC):
    """
    Interface for Internal Mechanics Actions.
    """

    @abstractmethod
    def registerIMA() -> dict:
        """
        Provides information on IMA name and properties.

        Returns:
            dict: {name: {required_actuators: [Actuator], IMA: class, action_type: class}}
        """
        raise NotImplementedError("RegisterIMA function not implemented.")

    @abstractmethod
    def execute(self, imam: object, goal_handle, **kw_actuators) -> bool:
        """
        Executes action.

        Args:
            imam (IMAM): imam
            goal_handle(): action goal handle

        Returns:
            success(bool): true-successfull, false-error
        """
        raise NotImplementedError("Execute function not implemented.")
