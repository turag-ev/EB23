"""
@Author: Robert Lange 
@Descripton: 
This class creats a A* pathfinder object, that recieves the [x,y] - coordinates of a start- and endpoint 
and returns a list of orders. The list of orders is later given to the driverclass 

To create the pathfinder object you have to provide two parameters: the diameter of the nodes of your grid in milimeters and the path
to the txt file which contains your grid
"""
import math
import numpy as np
from abc import ABC, abstractmethod


import os
import sys

# TODO: why do we need the following 3 lines? -> I don't think so (AH)
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

# TODO: I dont think we need this later since we won't return MovementOrders but just points, but we'll see later, I guess
from EB23_Enums import OrderType


class PathFinder(ABC):
    @abstractmethod
    def getMovementOrders():
        pass


# utilities ----------------------------------------
def clamp(x, down, up):
    if x < down:
        return down
    elif x > up:
        return up
    else:
        return x


def modSign(x):
    if x < 0:
        return -1
    elif x >= 0:
        return 1


# --------------------------------------------------


class Node:
    def __init__(
        self,
        _obstacleNode: bool,
        _walkable: bool,
        _worldPos: "tuple[int, int]",
        Grid_x: int,
        Grid_y: int,
    ) -> None:
        # determites if the node belongs to a static obstacle
        self.obstacleNode = _obstacleNode

        # determites if the node is blocked or not
        self.walkable = _walkable

        # position in the world coordinate system
        self.worldPosition = _worldPos

        # position in the grid matrix
        self.grid_x = Grid_x
        self.grid_y = Grid_y

        # distance between the current node and the start node
        self.gCost = 0

        # estimated distance from the current node to target node
        self.hCost = 0
        self.parent = None

        # only used in heap implementation, which is currently not used
        self.HeapIndex = int()

    def fCost(self):
        """
        info: calculates total cost of a node
        """
        return self.gCost + self.hCost

    def CompareTo(self, NodeToCompare):
        if self.fCost() < NodeToCompare.fCost():
            return 1
        elif self.fCost() == NodeToCompare.fCost:
            if self.hCost <= NodeToCompare.hCost:
                return 1
            else:
                return -1
        else:
            return -1

    def setWorldPosition(self, newWorldPostion: "tuple[int, int]") -> None:

        """
        info: sets the worldPosition of a node should only be used to correct the world position of the target node from the center to the actual coordinates of the target

        :param newWorldPosition:
            coordinates of the new world position
        :type newWorldPosition: tuple[int, int]
        """

        self.worldPosition = newWorldPostion

    def block(self) -> None:
        """
        info: sets the status od a node as blocked
        """
        self.walkable = False

    def free(self) -> None:
        """
        info: sets the status of a node as walkable
        """
        self.walkable = True

    def getGridPosition(self):
        """
        info: return position of node in the grid
        """
        return self.grid_x, self.grid_y

    def isObstacleNode(self) -> bool:
        """
        info: returns if the node belongs to an obstacle or not
        """
        return self.obstacleNode


class Grid:
    def __init__(self, NodeDiameter, _path):
        self.nodeDiameter = NodeDiameter
        self.worldSize = [0, 0]
        self.grid = self.getGrid(_path)
        self.enemyNodes = set()

    def getGrid(self, path):
        grid = []
        with open(path, "r") as f:
            data = f.readlines()
            self.gridSizeX = len(data)
            self.gridSizeY = len(data[0].split(";"))
            self.worldSize[0] = self.gridSizeX * self.nodeDiameter
            self.worldSize[1] = self.gridSizeY * self.nodeDiameter
        for n in range(0, self.gridSizeX):
            data_line = data[n].split(";")
            line = []
            for i in range(0, self.gridSizeY):
                data_line[i] = data_line[i].replace("(", " ")
                data_line[i] = data_line[i].replace(")", " ")
                data_line[i] = data_line[i].split(".")

                if int(data_line[i][1]) == 1:
                    line.append(
                        Node(
                            _obstacleNode=True,
                            _walkable=False,
                            _worldPos=(
                                float(data_line[i][0].replace(",", ".")),
                                float(data_line[i][2].replace(",", ".")),
                            ),
                            Grid_x=n,
                            Grid_y=i,
                        )
                    )
                else:
                    line.append(
                        Node(
                            _obstacleNode=False,
                            _walkable=True,
                            _worldPos=(
                                float(data_line[i][0].replace(",", ".")),
                                float(data_line[i][2].replace(",", ".")),
                            ),
                            Grid_x=n,
                            Grid_y=i,
                        )
                    )
            grid.append(line)
        return grid

    def getNeighbours(self, node, border):
        neighbours = []
        for x in range(-border, border + 1):
            for y in range(-border, border + 1):
                if x == 0 and y == 0:
                    continue
                checkX = node.gridX + x
                checkY = node.gridY + y

                if (
                    checkX >= 0
                    and checkX < self.gridSizeX
                    and checkY >= 0
                    and checkY < self.gridSizeY
                ):
                    neighbours.append(self.grid[checkX][checkY])
        return neighbours

    def NodeFromWorldPoint(self, worldPositionX, worldPositionY):
        percentX = worldPositionX / self.worldSize[0] + 0.5
        # print(percentX)
        percentY = worldPositionY / self.worldSize[1] + 0.5

        percentX = clamp(percentX, 0, 1)
        percentY = clamp(percentY, 0, 1)

        x = math.floor(min(self.gridSizeX * percentX, self.gridSizeX - 1))
        y = math.floor(min(self.gridSizeY * percentY, self.gridSizeY - 1))

        return self.grid[x][y]

    def blockEnemyLocation(self, x: int, y: int) -> None:
        """
        info: block the location of the enemy robot on the map

        :param x:
            x coordinate of the enemy robot on the map
        :type x: int

        :param y:
            y coordinate of the enemy robot on the map
        :type y: int
        """
        # get center node of enemy robot
        centerNode = self.NodeFromWorldPoint(x, y)

        # grid position of center node
        x, y = centerNode.getGridPosition()

        save = [5, 6, 7, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 7, 6, 5]
        saveIndex = 0

        # get enemy nodes
        for iy in range(y - 8, y + 9):

            for ix in range(x - save[saveIndex], x + save[saveIndex] + 1):

                if 0 <= ix < 60 and 0 <= iy < 40:
                    newNode = self.grid[ix][iy]
                    # print(newNode.worldPosition)
                    self.enemyNodes.add(newNode)

            saveIndex += 1

        # set those nodes as blocked
        for node in self.enemyNodes:
            node.block()

    def freeEnemyLocation(self) -> None:
        """
        info: clears the old enemy position
        """
        for node in self.enemyNodes:
            if not node.isObstacleNode():
                node.free()


class AstarPathfinder(PathFinder):
    def __init__(self, nodeDiameter, pathToGridFile) -> None:
        """
        info: an object is created which has the porpous to calculate a path from
        start coordinate to target coordinates and return a list of corresponding movement orders

        :functions getMovementOrders:
            returns list of movement orders to drive from start to target

        :param nodeDiameter:
            diameter of nodes in relation to the coordinate system used:
                coordinate system in mm --> nodeDiameter in mm
                coordinate system in cm --> nodeDiameter in cm
        :type nodeDiameter: int

        :param pathToGridFile:
            path to location at which the file of the grid is stored
        :type pathToGridFile: str
        """
        self.grid = Grid(nodeDiameter, pathToGridFile)

        # radius (in milimeter since the coordinate system is in milimeter) used to model the enemy robot as a circle

    def __GetDistance(self, nodeA, nodeB):
        distX = abs(nodeA.gridX - nodeB.gridX)
        distY = abs(nodeA.gridY - nodeB.gridY)

        if distX > distY:
            return 14 * distY + 10 * (distX - distY)
        else:
            return 14 * distX + 10 * (distY - distX)

    def __FindPath(self, _start, _target):
        startNode = self.grid.NodeFromWorldPoint(_start[0], _start[1])
        targetNode = self.grid.NodeFromWorldPoint(_target[0], _target[1])
        targetNode.gridX
        targetNode.gridY

        # print(self.targetNode.gridX)
        openSet = []
        # openSet = Heap()
        closedSet = []

        openSet.append(startNode)
        # openSet.add(startNode)
        # openSet.append(self.startNode)
        # while openSet.Count() > 0:
        while len(openSet) > 0:
            # currentNode = openSet.RemoveFirst()

            currentNode = openSet[0]
            for i in openSet:
                if (
                    i.fCost() < currentNode.fCost()
                    or i.fCost() == currentNode.fCost()
                    and i.hCost < currentNode.hCost
                ):
                    currentNode = i

            openSet.remove(currentNode)

            closedSet.append(currentNode)

            if currentNode == targetNode:
                path = self.__RetracePath(startNode, targetNode)
                return path

            neighbours = self.grid.getNeighbours(currentNode, 1)
            for n in neighbours:

                if n.walkable == False or n in closedSet:
                    continue

                newMovementCostToNeighbour = currentNode.gCost + self.__GetDistance(
                    currentNode, n
                )
                # if newMovementCostToNeighbour < n.gCost or not (openSet.Contains(n)):
                if newMovementCostToNeighbour < n.gCost or not n in openSet:
                    n.gCost = newMovementCostToNeighbour
                    n.hCost = self.__GetDistance(n, targetNode)
                    n.parent = currentNode
                    # if not openSet.Contains(n):
                    if not n in openSet:
                        openSet.append(n)
                        # openSet.add(n)

    def __RetracePath(
        self, startNode: "tuple[int, int]", targetNode: "tuple[int, int]"
    ):

        """
        info: retrace the found path from the targetNode to the startNode

        :param startNode:
            coordinates of the start node
        :type startNode: tuple[int, int]

        :param targetNode:
            coordinates of the target node
        :type targetNode: tuple[int, int]
        """

        path = []
        currentNode = targetNode
        while currentNode != startNode:
            path.append(currentNode)
            currentNode = currentNode.parent
        path.reverse()
        return path

    # To-Dos:
    # Predicting the position of the enemy and knowing the position of our bot ???
    # remove useless nodes ???
    # splines between 2 points ???
    # get the best splines ???
    # offset start and end (what do i return to LMC? real coordiantes? -> if yes not spline between first node and last node, but start position and end position) ???
    # strange splines if angle between points is big ???

    def getSplinesFromPoints(self):
        # get from driving-unit
        pass

    def getAngleBetweenToNodes(self, node1: Node, node2: Node):
        """Function for calculating the angle of the connecting line between two nodes.

        Args:
            node1 (Node): node from where the connecting line starts
            node2 (Node): node where the connecting line ends
        """
        # calculate the x- and y-difference between those two nodes:
        deltaGrid_x = node2.grid_x - node1.grid_x
        deltaGrid_y = node2.grid_y - node1.grid_y
        # atan() returns radians -> by converting to de: if left: 180, if up: 90, if right: 0, if down: -90:
        angle = math.atan2(deltaGrid_y, deltaGrid_x) / (2 * math.pi) * 180
        return angle

    def removeUselessNodes(self, list_of_nodes: list[Node]):
        """Function for removing the useless nodes (the nodes, where the direction doesn't change) from the list of nodes.
            The direction doesn't change if the angle of the connecting line between the last and the current and the current
            and the next doesn't change.

        Args:
            list_ofNodes (list[node]): original list of nodes, which is returned by the D*-algorithms
        """

        for i in range(1, list_of_nodes):
            # if angle between the last and the current == angle between the current and the next:
            if self.getAngleBetweenToNodes(
                list_of_nodes[i - 1], list_of_nodes[i]
            ) == self.getAngleBetweenToNodes(list_of_nodes[i], list_of_nodes[i + 1]):
                list_of_nodes.remove(list_of_nodes[i])  # remove current node

    def splineColidesWithObstacle(self, spline: list(int), grid: Grid):
        pass

    def getBestSupportingPoints(self, list_of_nodes, grid):
        """Function for getting the best spline path from our start point to our end point depending on the list of nodes.
            First, we look if we can just connect start and end point with a spline. If that's not possible, we check if we can
            connect the start node with the penultimate node (node before the last one) with a spline and so on... ???


        Args:
            list_of_nodes (list[node]): list of the important (usefull) nodes
            grid (_type_): _description_ ???
        """
        pass

    def getMovementOrders(
        self,
        startOrientation: int,
        start: "tuple[int, int]",
        target: "tuple[int, int]",
        targetOrientation: int,
        enemyPositionList: "list[tuple[int, int]]",
    ) -> "list[list[int, int]]":

        """
        info: Returns a list of orders. A orders is structured like: [angles to turn in degree, "forward"]
            --> negative angles mean turn right, positive angles mean turn left

        :param startOrientation:
            orientation of the robot at the start position from -180 (left turn) to 180 (right turn)
        :type startOrientation: int

        :param start:
            coordinates of the start position
        :type start: tuple[int, int]

        :param target:
            coordinates of the target position
        :type target: tuple[int, int]

        :param targetOrientation:
            orientation the robot should have at the target position from -180 (left turn) to 180 (right turn)
        :type targetOrientation: int

        :param enemyPosition:
            location of the enemy, set equal to None if position is unknown
        :type enemyPosition: tuple[int, int] or None
        """
        # clear the old enemy position
        self.grid.freeEnemyLocation()

        # block new enemy position
        if type(enemyPositionList) != type(None):
            for enemyPosition in enemyPositionList:
                self.grid.blockEnemyLocation(enemyPosition[0], enemyPosition[1])

        # get path from start and target
        nodeList = self.__FindPath(start, target)
        Movements = []

        # if nodeList is equal to none than there is no possible path
        if nodeList == None:
            return None, None

        if len(nodeList) == 0:
            if start == target:
                skip = True
            else:
                # add target node
                nodeList.append(Node(False, True, target, 0, 0))

                skip = False
        else:
            # change the coordinates of the last node from the center to the actual target coordinates
            nodeList[len(nodeList) - 1].setWorldPosition(target)
            skip = False

        # set up
        currentOrientation = startOrientation
        xAlt = start[0]
        yAlt = start[1]
        distanceOfPath = 0

        if not skip:
            # turn node list in movement orders
            for i in range(0, len(nodeList)):

                # get world coordinates of node
                xNeu = nodeList[i].worldPosition[0]
                yNeu = nodeList[i].worldPosition[1]

                # calculate rotation and distance to new node
                rotation = np.arctan2(yNeu - yAlt, xNeu - xAlt) * 180 / np.pi
                distance = np.sqrt(
                    np.power((xNeu - xAlt), 2) + np.power((yNeu - yAlt), 2)
                )

                # calculate rotation the robot has to do
                newRotation = rotation - currentOrientation
                if newRotation < -180:
                    newRotation = 360 + newRotation
                elif newRotation > 180:
                    newRotation = newRotation - 360
                # if rotation == 180:
                #    newRotation = modSign(currentOrientation) * newRotation

                """ change distance to OrderType 
                if distance == 50:
                    Movements.append([int(newRotation), OrderType.FORWARD])
                else:
                    Movements.append([int(newRotation), OrderType.DIAGONAL_FORWARD])
                """

                # add movement order to list
                Movements.append([newRotation, distance])

                # update
                currentOrientation = rotation
                xAlt = xNeu
                yAlt = yNeu
                distanceOfPath += distance

        # if the last orientation of the robot doesnt equals the desired target orientation add corresponding movement order
        if currentOrientation != targetOrientation:
            newRotation = targetOrientation - currentOrientation
            if newRotation < -180:
                newRotation = 360 + newRotation
            elif newRotation > 180:
                newRotation = newRotation - 360
            # if targetOrientation == 180:
            #    newRotation = modSign(currentOrientation) * newRotation
            Movements.append([int(newRotation), 0])

        # maybe add the distance of the path to return values
        return Movements, distanceOfPath


# not working :(
class _Heap:
    def __init__(self) -> None:
        self.items = []
        self.currentItemCount = 0

    def add(self, item):
        item.HeapIndex = self.currentItemCount
        self.items.append(item)
        self.SortUp(item)
        self.currentItemCount = self.currentItemCount + 1

    def RemoveFirst(self):
        firstItem = self.items[0]
        self.currentItemCount = self.currentItemCount - 1
        self.items[0] = self.items[self.currentItemCount]
        self.items[0].HeapIndex = 0
        self.items.pop(self.currentItemCount)
        if len(self.items) > 0:
            self.SortDown(self.items[0])
        return firstItem

    def SortDown(self, item):
        while True:
            childIndexLeft = item.HeapIndex * 2 + 1
            childIndexRigth = item.HeapIndex * 2 + 2
            swapIndex = 0

            if childIndexLeft < self.currentItemCount:
                swapIndex = childIndexLeft

                if childIndexRigth < self.currentItemCount:
                    if (
                        self.items[childIndexLeft].CompareTo(
                            self.items[childIndexRigth]
                        )
                        < 0
                    ):  # kleiner als 0 --> LeftChild hat größere fCost als RigthChild, mit kleinerer fCost soll getauscht werden
                        swapIndex = childIndexRigth

                if (
                    item.CompareTo(self.items[swapIndex]) < 0
                ):  # hat eins der Kinder eine kleinere fCost wird getauscht
                    self.Swap(item, self.items[swapIndex])
                else:
                    return

            else:
                return

    def Contains(self, item):
        if len(self.items) > 0 and self.items[item.HeapIndex] == item:
            return True
        else:
            return False

    def UpdateItem(self, item):
        self.SortUp(item)

    def Count(self):
        return self.currentItemCount

    def SortUp(self, item):
        parentIndex = int((item.HeapIndex - 1) / 2)
        while True:
            parentItem = self.items[parentIndex]
            if item.CompareTo(parentItem) > 0:
                self.Swap(item, parentItem)
            else:
                break

            parentIndex = int((item.HeapIndex - 1) / 2)

    def Swap(self, itemA, itemB):
        self.items[itemA.HeapIndex] = itemB
        self.items[itemB.HeapIndex] = itemA

        itemAIndex = itemA.HeapIndex
        itemA.HeapIndex = itemB.HeapIndex
        itemB.HeapIndex = itemAIndex


if __name__ == "__main__":
    root_folder = os.path.dirname(os.path.abspath(__file__))

    pf = AstarPathfinder(50, f"{root_folder}/SpielfeldGridSmallObstacle.txt")

    # grid = Grid(50, "./Main/Pathfinding/SpielfeldGrid.txt")
    # grid.blockEnemyLocation(100, 100)
    # grid.freeEnemyLocation()

    # path, length = pf.getMovementOrders(180, (0, 0), (-1120, -480), 135, None)
    path, length = pf.getMovementOrders(90, (-1143, -546), (-1175, 675), 90, None)
    print(path)

    input("press enter to continue")
    path, length = pf.getMovementOrders(-90, (-507, -134), (-1175, 567), 90, None)
    print(path)
    # pointsOnCircle = pf.calculateCircle(100, 100)
    # print(pointsOnCircle)

    """ visulazation 
    import matplotlib.pyplot as plt
    from matplotlib.patches import Rectangle
    plt.xlabel("X")
    plt.ylabel("Y")
    fig, ax = plt.subplots()
    plt.title("Point plot")
    for point in pointsOnCircle: 
        plt.scatter(point[0], point[1])
        ax.add_patch(Rectangle((point[0] - 25, point[1] - 25), 50, 50))
         
    plt.show()
    """

    # path = pf.getMovementOrders(-90, (0, 0), (0, 0), -90)
    # print(path)
