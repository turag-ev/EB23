from abc import ABC, abstractmethod
from EB23_Enums import Actor


class IMA_Interface(ABC):
    """
    Interface for Internal Mechanics Actions.
    """

    used_actors: list[Actor]

    @abstractmethod
    def execute(self):
        pass
