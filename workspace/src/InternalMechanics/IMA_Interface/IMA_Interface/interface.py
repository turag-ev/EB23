from abc import ABC, abstractmethod


class IMA_Interface(ABC):
    """
    Interface for Internal Mechanics Actions.
    """

    used_actors: list[str]

    @abstractmethod
    def execute(self):
        pass
