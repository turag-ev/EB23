from abc import ABC, abstractmethod


class GameAction(ABC):
    """
    Abstract base class for game actions.
    """

    def __init__(self, id: str):
        self.id = id

    @abstractmethod
    def setup(config):
        pass

    @abstractmethod
    def checkExecutability(self, state) -> bool:
        pass

    # TODO Consider using union type instead of kw_args
    @abstractmethod
    def preProcess(self, **kw_args):
        pass

    @abstractmethod
    def process(self, **kw_args):
        pass

    @abstractmethod
    def postProcess(self, **kw_args):
        pass
