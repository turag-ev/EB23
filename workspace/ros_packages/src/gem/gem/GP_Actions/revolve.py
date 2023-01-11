from GP_Interface import GameAction


class Revolve(GameAction):
    """
    Interface for revolve game action.
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
