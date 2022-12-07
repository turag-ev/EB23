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


class PickUp(GameAction):
    """
    Interface for pick-up game action.
    """

    def setup(config):
        return

    def checkExecutability(self, state) -> bool:
        return True

    def preProcess(self, **kw_args):
        pass

    def process(self, **kw_args):
        pass

    def postProcess(self, **kw_args):
        pass


class Store(GameAction):
    """
    Interface for store game action.
    """

    def setup(config):
        return

    def checkExecutability(self, state) -> bool:
        return True

    def preProcess(self, **kw_args):
        pass

    def process(self, **kw_args):
        pass

    def postProcess(self, **kw_args):
        pass

