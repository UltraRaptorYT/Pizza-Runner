from turtle import RawTurtle
import time
from Algorithm.AStar import AStar
from Algorithm.BreadthFirstSearch import BreadthFirstSearch
from Algorithm.DepthFirstSearch import DepthFirstSearch
from Algorithm.Greedy import Greedy

# Mapping Directions
DIRECTION_MAP = {
    0: "EAST",
    90: "NORTH",
    180: "WEST",
    270: "SOUTH"
}

# Mapping Index
INDEX_MAP = {
    "EAST": (0, 1),
    "NORTH": (-1, 0),
    "WEST": (0, -1),
    "SOUTH": (1, 0)
}


class Character(RawTurtle):
    def __init__(self, maze, canvas=None, x=0, y=0, size=40):
        super().__init__(canvas)
        self.canvas = canvas
        self.hideturtle()
        self.shape('turtle')
        self.pencolor('black')
        self.penup()
        self.x = x
        self.y = y
        self.setpos(x, y)
        self.maze = maze
        self.showturtle()
        self.size = size
        self.shapesize(size / 40)
        self.setheading(0)
        self.facing = DIRECTION_MAP[self.heading()]
        self.startX = x
        self.startY = y
        self.currentIndex = [int((self.maze.startY - self.y) /
                             self.size), int((self.x - self.maze.endX)/self.size)]
        self.state = False
        self.step = 0

    # Basic Functions for algorithms
    def turnLeft(self):
        self.left(90)
        self.facing = DIRECTION_MAP[self.heading()]

    def turnRight(self):
        self.right(90)
        self.facing = DIRECTION_MAP[self.heading()]

    def goForward(self):
        validPath, isEnd = self.checkAdj()
        if isEnd:
            print("End")
        if validPath:
            self.currentIndex = validPath
            self.step += 1
            self.forward(self.size)

    # Basic movement for Free Roam
    def moveLeft(self):
        if self.facing == "NORTH":
            self.turnLeft()
        elif self.facing == "SOUTH":
            self.turnRight()
        elif self.facing == "EAST":
            self.left(90)
            self.turnLeft()
        elif self.facing == "WEST":
            self.facing = DIRECTION_MAP[self.heading()]
        self.goForward()

    def moveRight(self):
        if self.facing == "NORTH":
            self.turnRight()
        elif self.facing == "SOUTH":
            self.turnLeft()
        elif self.facing == "WEST":
            self.right(90)
            self.turnRight()
        elif self.facing == "EAST":
            self.facing = DIRECTION_MAP[self.heading()]
        self.goForward()

    def moveForward(self):
        if self.facing == "EAST":
            self.turnLeft()
        elif self.facing == "SOUTH":
            self.left(90)
            self.turnLeft()
        elif self.facing == "WEST":
            self.turnRight()
        elif self.facing == "NORTH":
            self.facing = DIRECTION_MAP[self.heading()]
        self.goForward()

    def moveDown(self):
        if self.facing == "EAST":
            self.turnRight()
        elif self.facing == "NORTH":
            self.right(90)
            self.turnRight()
        elif self.facing == "WEST":
            self.turnLeft()
        elif self.facing == "SOUTH":
            self.facing = DIRECTION_MAP[self.heading()]
        self.goForward()

    # Checking for walls
    def checkAdj(self, direction=None):
        if direction is None:
            direction = self.facing
        movingIndex = list(self.currentIndex)
        movingIndex[0] += INDEX_MAP[direction][0]
        movingIndex[1] += INDEX_MAP[direction][1]
        checkTile = self.maze.get_mapArr()[movingIndex[0]][movingIndex[1]]
        if checkTile.is_wall():
            return [False, False]
        elif checkTile.is_end():
            return [movingIndex, True]
        else:
            return [movingIndex, False]

    # Update state of character
    def updateState(self, newState=None):
        # Arrows Key
        self.canvas.onkey(None, "Left")
        self.canvas.onkey(None, "Right")
        self.canvas.onkey(None, "Up")
        self.canvas.onkey(None, "Down")
        # WASD Key
        self.canvas.onkey(None, "a")
        self.canvas.onkey(None, "d")
        self.canvas.onkey(None, "w")
        self.canvas.onkey(None, "s")
        self.canvas.onkeypress(None, "p")
        if not newState is None:
            self.state = newState
        else:
            self.state = not self.state
        return self.state

    # Color block
    def colorCell(self, index, colorFunc=None):
        time.sleep(0.01)
        block = self.maze.get_mapArr()[index[0]][index[1]]
        if colorFunc:
            eval(f"block.{colorFunc}()")
            block.draw()
            return
        elif not block.is_wall() and not colorFunc:
            block.make_open()
            block.draw()
            return

    # Start button setting the default algorithm to Left Hand Rule
    def start(self, algorithm="Left Hand Rule", firstTime=False):
        if self.pos() != (self.startX, self.startY) or not firstTime:
            self.reset_everything()
            time.sleep(0.5)
        self.shapesize(self.size / 40)
        self.step = 0
        self.algorithm = algorithm
        self.seen = []
        self.state = True
        self.move = []
        self.__roam = False
        self.hideturtle()
        if algorithm == "Left Hand Rule":
            if len(self.maze.get_mapArr()[
                      self.currentIndex[0]][self.currentIndex[1]].neighbors) == 4:
                while self.checkAdj()[0] and not self.checkAdj()[1]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj()[0], "make_path")
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj()[0]
            while not self.checkAdj()[1]:
                if len(self.seen) > 0 and (self.currentIndex == [int((self.maze.startY - self.y) /
                                                                     self.size), int((self.x - self.maze.endX)/self.size)] or self.seen.count(self.currentIndex) >= 3):
                    break
                directionList = list(INDEX_MAP.keys())
                # checkLeft wall
                leftIndex = directionList[(directionList.index(
                    self.facing) + 1) % len(directionList)]
                if self.checkAdj(leftIndex)[0]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj(leftIndex)[0], "make_path")
                    self.move.append(self.turnLeft)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(leftIndex)[0]
                    self.turnLeft()
                else:
                    # checkFront wall
                    if self.checkAdj()[0]:
                        self.seen.append(self.currentIndex)
                        self.colorCell(self.checkAdj()[0], "make_path")
                        self.move.append(self.goForward)
                        self.currentIndex = self.checkAdj()[0]
                    else:
                        self.move.append(self.turnRight)
                        self.turnRight()
            if self.checkAdj()[1]:
                self.currentIndex = self.checkAdj()[0]
                self.move.append(self.goForward)
        # Switching algorithm to Right Hand Rule
        elif algorithm == "Right Hand Rule":
            if len(self.maze.get_mapArr()[
                      self.currentIndex[0]][self.currentIndex[1]].neighbors) == 4:
                while self.checkAdj()[0] and not self.checkAdj()[1]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj()[0], "make_path")
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj()[0]
            while not self.checkAdj()[1]:
                if len(self.seen) > 0 and (self.currentIndex == [int((self.maze.startY - self.y) /
                                                                    self.size), int((self.x - self.maze.endX)/self.size)] or self.seen.count(self.currentIndex) >= 3):
                    break
                directionList = list(INDEX_MAP.keys())
                # checkRight wall
                rightIndex = directionList[(directionList.index(
                    self.facing) - 1) % len(directionList)]
                if self.checkAdj(rightIndex)[0]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj(rightIndex)[0], "make_path")
                    self.move.append(self.turnRight)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(rightIndex)[0]
                    self.turnRight()
                else:
                    # checkFront wall
                    if self.checkAdj()[0]:
                        self.seen.append(self.currentIndex)
                        self.colorCell(self.checkAdj()[0], "make_path")
                        self.move.append(self.goForward)
                        self.currentIndex = self.checkAdj()[0]
                    else:
                        self.move.append(self.turnLeft)
                        self.turnLeft()
            if self.checkAdj()[1]:
                self.currentIndex = self.checkAdj()[0]
                self.move.append(self.goForward)
        elif algorithm == "Breadth First Search":
            algo = BreadthFirstSearch(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        elif algorithm == "Depth First Search":
            algo = DepthFirstSearch(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        elif algorithm == "A* Search":
            algo = AStar(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        elif algorithm == "Greedy Best First Search":
            algo = Greedy(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        # Switch to Free Roam
        elif algorithm == "Free Roam":
            self.__roam = True
            self.pendown()
            self.showturtle()
            while not self.maze.get_mapArr()[self.currentIndex[0]][self.currentIndex[1]].is_end() and self.state:
                directionList = list(INDEX_MAP.keys())
                # Arrows Key
                self.canvas.onkey(self.moveLeft, "Left")
                self.canvas.onkey(self.moveRight, "Right")
                self.canvas.onkey(self.moveForward, "Up")
                self.canvas.onkey(self.moveDown, "Down")
                # WASD Key
                self.canvas.onkey(self.moveLeft, "a")
                self.canvas.onkey(self.moveRight, "d")
                self.canvas.onkey(self.moveForward, "w")
                self.canvas.onkey(self.moveDown, "s")
                self.canvas.onkey(self.updateState, "p")
                if not self.state:
                    self.penup()
                    break
                self.canvas.listen()
                self.canvas.mainloop()
        self.showturtle()
        if not self.__roam and algorithm in ["Left Hand Rule", "Right Hand Rule"]:
            self.setheading(0)
            self.facing = DIRECTION_MAP[self.heading()]
            print(self.currentIndex)
            self.pendown()
            if not self.maze.get_mapArr()[
                    self.currentIndex[0]][self.currentIndex[1]].is_end():
                self.state = False
                print("Invalid Maze")
                return False
            self.currentIndex = [int((self.maze.startY - self.y) /
                                     self.size), int((self.x - self.maze.endX)/self.size)]
            for steps in self.move:
                steps()
                time.sleep(0.01)
            self.penup()
        elif not self.__roam and algorithm in ["Breadth First Search", "Depth First Search", "A* Search", "Greedy Best First Search"]:
            self.setheading(0)
            self.facing = DIRECTION_MAP[self.heading()]
            self.currentIndex = [int((self.maze.startY - self.y) /
                                     self.size), int((self.x - self.maze.endX)/self.size)]
            path = self.move
            if path is None:                
                self.state = False
                self.penup()
                return False
            self.move = []
            currentBlock = path[-1]  # Initialise currentBlock as start
            for idx, pathBlock in enumerate(path):
                # self.move()
                if not pathBlock.is_start():
                    for [facing, index] in INDEX_MAP.items():
                        if [currentBlock.row + index[0],
                            currentBlock.col + index[1]] == [path[len(path) - 2 - idx].row,
                                                             path[len(path) - 2 - idx].col]:
                            while list(INDEX_MAP.keys()).index(self.facing) != list(INDEX_MAP.keys()).index(facing):
                                diff = list(INDEX_MAP.keys()).index(
                                    facing) - list(INDEX_MAP.keys()).index(self.facing)
                                if (diff > 0 and diff != len(INDEX_MAP.keys()) - 1) or diff == -(len(INDEX_MAP.keys()) - 1):
                                    self.turnLeft()
                                    self.move.append(self.turnLeft)
                                else:
                                    self.turnRight()
                                    self.move.append(self.turnRight)
                            currentBlock = path[len(path) - 2 - idx]
                            self.move.append(self.goForward)
                if pathBlock.is_end() or pathBlock.is_start():
                    continue
                pathBlock.make_path()
                pathBlock.draw()
                time.sleep(0.01)
            self.setheading(0)
            self.facing = DIRECTION_MAP[self.heading()]
            self.pendown()
            self.currentIndex = [int((self.maze.startY - self.y) /
                                     self.size), int((self.x - self.maze.endX)/self.size)]
            for steps in self.move:
                steps()
                time.sleep(0.01)
            self.penup()
        self.state = False
        self.penup()
        return True
    # Resetting state of maze and turtle

    def reset_everything(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.setpos(int(self.startX), int(self.startY))
        self.shapesize(self.size / 40)
        self.x = self.startX
        self.y = self.startY
        self.currentIndex = [int((self.maze.startY - self.y) /
                                 self.size), int((self.x - self.maze.endX)/self.size)]
        self.setheading(0)
        self.facing = DIRECTION_MAP[self.heading()]
        self.maze.reset()
        self.showturtle()
