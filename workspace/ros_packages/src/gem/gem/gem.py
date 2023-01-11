from random import randrange
from EB23_Enums.GEM_enums import GameActionEnum
import rclpy
from rclpy.node import Node
import queue
from .GP_Actions.pickup import PickUp
from .GP_Actions.store import Store
from .GP_Actions.retrieve import Retrieve
from .GP_Actions.drop import Drop
from .GP_Actions.revolve import Revolve
from GP_Interface.interfaces import GameAction


class GEM(Node):
    def __init__(self):
        super().__init__("gem")
        self.prios = {
            GameActionEnum.PICK_UP: 90,
            GameActionEnum.STORE: 70,
            GameActionEnum.RETRIEVE: 50,
            GameActionEnum.DROP: 30,
            GameActionEnum.REVOLVE: 10,
        }

        self.enum_prios: list = list(self.prios.keys())
        self.next_index = 0
        self.q = queue.Queue(maxsize=10)

    def queueAction(self, state):
        if self.q.full():
            self.get_logger().info("Game action queue is full. Aborting queue task.")
            return

        action: GameAction = self.nextActionObject()
        if action.checkExecutability(state):
            self.get_logger().info("Queueing game action " + str(action))
            self.q.put(action)

        self.next_index = (self.next_index + 1) % len(self.enum_prios)
        self.get_logger().info("New game action index: " + str(self.next_index))

    def nextActionObject(self) -> GameAction:
        next_action: GameActionEnum = self.enum_prios[self.next_index]
        if next_action == GameActionEnum.PICK_UP:
            return PickUp("pick_up_" + self.pseudoRand())
        if next_action == GameActionEnum.STORE:
            return Store("store_" + self.pseudoRand())
        if next_action == GameActionEnum.RETRIEVE:
            return Retrieve("retrieve_" + self.pseudoRand())
        if next_action == GameActionEnum.DROP:
            return Drop("drop_" + self.pseudoRand())
        return Revolve("revolve_" + self.pseudoRand())

    def pseudoRand(self) -> str:
        return str(randrange(400))


def main():
    rclpy.init(args=None)
    gem = GEM()
    i: int = 0
    while i < 12:
        gem.queueAction(state="")
        i += 1
    rclpy.spin(gem)


if __name__ == "__main__":
    main()
