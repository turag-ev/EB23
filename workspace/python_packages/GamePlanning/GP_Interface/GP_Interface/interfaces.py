class PickUp():
    """
    Interface for pick-up game action.
    """
    def __init__(self):
        return

    def setup(config):
        return

    def checkExecutability(self, state) -> bool:
        return True

    @abstractmethod
    def preProcess(self, **kw_actuators):
        pass

    @abstractmethod
    def process(self, **kw_actuators):
        pass

    @abstractmethod
    def postProcess(self, **kw_actuators):
        pass


class Store():
    """
    Interface for store game action.
    """
    def __init__(self):
        return

    def setup(config):
        return

    def checkExecutability(self, state) -> bool:
        return True

    @abstractmethod
    def preProcess(self, **kw_actuators):
        pass

    @abstractmethod
    def process(self, **kw_actuators):
        pass

    @abstractmethod
    def postProcess(self, **kw_actuators):
        pass