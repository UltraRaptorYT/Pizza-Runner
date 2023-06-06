"""
Member 1:
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
Member 2:
Name: Samuel Tay Tze Ming
Class: DAAA/FT/2B/01
Admin No.: P2107404
"""

from turtle import RawTurtle
import time
from Algorithm.AStar import AStar
from Algorithm.BreadthFirstSearch import BreadthFirstSearch
from Algorithm.DepthFirstSearch import DepthFirstSearch
from Algorithm.Greedy import Greedy

# Mapping Directions ~ Hong Yu + Samuel
DIRECTION_MAP = {
    0: "EAST",
    90: "NORTH",
    180: "WEST",
    270: "SOUTH",
    360: "EAST"
}

# Mapping Index
INDEX_MAP = {
    "EAST": (0, 1),
    "NORTH": (-1, 0),
    "WEST": (0, -1),
    "SOUTH": (1, 0)
}

# Create Character class inherit from RawTurtle
class Character(RawTurtle):
    def __init__(self, maze, canvas=None, x=0, y=0, size=40):
        super().__init__(canvas)
        self.canvas = canvas
        self.hideturtle()
        # Set shape
        self.shape('turtle')
        self.pencolor('black')
        self.penup()
        # Set maze
        self.maze = maze
        # Set size and heading
        self.size = size
        self.shapesize(size / 40)
        self.setheading(0)
        self.facing = DIRECTION_MAP[round(self.heading())]
        # Set position
        self.setpos(x, y)
        self.x = x
        self.y = y
        self.startX = x
        self.startY = y
        self.currentIndex = [int((self.maze.startY - self.y) /
                             self.size), int((self.x - self.maze.endX)/self.size)]
        # Set state
        self.state = False
        # Set step
        self.step = 0
        self.showturtle()


    # Basic Functions for algorithms
    # Turn Left
    def turnLeft(self):
        self.left(90)
        self.facing = DIRECTION_MAP[round(self.heading())]

    # Turn Right
    def turnRight(self):
        self.right(90)
        self.facing = DIRECTION_MAP[round(self.heading())]

    # Go Forward
    def goForward(self):
        validPath, isEnd = self.checkAdj()
        # Check adjacent values
        if isEnd:
            print("End")
        # If valid path then move forward
        if validPath:
            self.currentIndex = validPath
            self.step += 1
            self.forward(self.size)

    # Basic movement for Free Roam
    # Move Left
    def moveLeft(self):
        if self.facing == "NORTH":
            self.turnLeft()
        elif self.facing == "SOUTH":
            self.turnRight()
        elif self.facing == "EAST":
            self.turnLeft()
            self.turnLeft()
        elif self.facing == "WEST":
            self.facing = DIRECTION_MAP[round(self.heading())]
        self.goForward()
        
    # Move Right
    def moveRight(self):
        if self.facing == "NORTH":
            self.turnRight()
        elif self.facing == "SOUTH":
            self.turnLeft()
        elif self.facing == "WEST":
            self.turnRight()
            self.turnRight()
        elif self.facing == "EAST":
            self.facing = DIRECTION_MAP[round(self.heading())]
        self.goForward()
        
    # Move Forward
    def moveForward(self):
        if self.facing == "EAST":
            self.turnLeft()
        elif self.facing == "SOUTH":
            self.turnLeft()
            self.turnLeft()
        elif self.facing == "WEST":
            self.turnRight()
        elif self.facing == "NORTH":
            self.facing = DIRECTION_MAP[round(self.heading())]
        self.goForward()
        
    # Move Down
    def moveDown(self):
        if self.facing == "EAST":
            self.turnRight()
        elif self.facing == "NORTH":
            self.turnRight()
            self.turnRight()
        elif self.facing == "WEST":
            self.turnLeft()
        elif self.facing == "SOUTH":
            self.facing = DIRECTION_MAP[round(self.heading())]
        self.goForward()
        
    # Update Position
    def update_pos(self, x, y):
        self.startX = x
        self.startY = y
        self.currentIndex = [int((self.maze.startY - self.y) /
                             self.size), int((self.x - self.maze.endX)/self.size)]

    # Checking for adjacent walls
    def checkAdj(self, direction=None):
        if direction is None:
            direction = self.facing
        movingIndex = list(self.currentIndex)
        movingIndex[0] += INDEX_MAP[direction][0]
        movingIndex[1] += INDEX_MAP[direction][1]
        if movingIndex[0] <= -1 or movingIndex[1] <= -1 or movingIndex[0] >= self.maze.rows or movingIndex[1] >= self.maze.columns:
            return [False, False]
        try:
            checkTile = self.maze.get_mapArr()[movingIndex[0]][movingIndex[1]]
            if checkTile.is_wall():
                return [False, False]
            elif checkTile.is_end():
                return [movingIndex, True]
            else:
                return [movingIndex, False]
        except IndexError:
            return [False, False]

    # Update state of character
    def updateState(self):
        # Arrows Key
        self.canvas.onkey(None, "Left")
        self.canvas.onkey(None, "Right")
        self.canvas.onkey(None, "Up")
        self.canvas.onkey(None, "Down")                
        self.state = False
        return self.state

    # Color block
    def colorCell(self, index, colorFunc=None):
        time.sleep(0.01)
        if not self.state:
            return
        block = self.maze.get_mapArr()[index[0]][index[1]]
        if block.is_start() or block.is_end():
            return
        # Change color if colorFunc is specified
        if colorFunc:
            eval(f"block.{colorFunc}()")
            block.draw()
            return
        # Check if value is a value path
        elif not block.is_wall() and not colorFunc:
            block.make_open()
            block.draw()
            return

    # Start button setting the default algorithm to Left Hand Rule
    def start(self, algorithm="Left Hand Rule", firstTime=False):
        # Check if reset needs to be done
        if self.pos() != (self.startX, self.startY) or not firstTime:
            self.reset_everything()
            time.sleep(0.5)
        # Reinitiate size and turtle movement
        self.shapesize(self.size / 40)
        self.step = 0
        self.algorithm = algorithm
        # Update state etc
        self.state = True
        self.seen = []
        self.move = []
        self.__roam = False
        self.hideturtle()
        self.setheading(0)
        self.facing = DIRECTION_MAP[round(self.heading())]
        self.currentIndex = [int((self.maze.startY - self.y) /
                                self.size), int((self.x - self.maze.endX)/self.size)]
        # Check algorithm
        if algorithm == "Left Hand Rule":
            # Check if neighbor len == 0
            if len(self.maze.get_mapArr()[
                      self.currentIndex[0]][self.currentIndex[1]].neighbors) == 0:
                self.showturtle()
                self.state = False
                print("Invalid Maze")
                return False
            # Check if neighbor len == 4
            if len(self.maze.get_mapArr()[
                      self.currentIndex[0]][self.currentIndex[1]].neighbors) == 4:
                # Move forward until hit wall or reach end
                while self.checkAdj()[0] and not self.checkAdj()[1]:
                    self.seen.append(self.currentIndex)
                    # Color cell
                    self.colorCell(self.checkAdj()[0], "make_path")
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj()[0]
            # Repeat while not reach end
            while not self.checkAdj()[1]:
                # Check if path has been walked more than 3 times then exit
                if len(self.seen) > 0 and self.seen.count(self.currentIndex) >= 3:
                    break
                # Choose direction
                directionList = list(INDEX_MAP.keys())
                # checkLeft wall
                leftIndex = directionList[(directionList.index(
                    self.facing) + 1) % len(directionList)]
                # If front is end, move forward
                if self.checkAdj()[1]:
                    self.currentIndex = self.checkAdj()[0]
                    self.move.append(self.goForward)
                    break
                # If left is end, turn left and move forward
                if self.checkAdj(leftIndex)[0] and self.checkAdj(leftIndex)[1]:
                    self.move.append(self.turnLeft)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(leftIndex)[0]
                    self.turnLeft()
                    break
                # Check if left wall is empty
                if self.checkAdj(leftIndex)[0]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj(leftIndex)[0], "make_path")
                    self.move.append(self.turnLeft)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(leftIndex)[0]
                    self.turnLeft()
                else:
                    # checkFront wall is empty
                    if self.checkAdj()[0]:
                        self.seen.append(self.currentIndex)
                        self.colorCell(self.checkAdj()[0], "make_path")
                        self.move.append(self.goForward)
                        self.currentIndex = self.checkAdj()[0]
                    else:
                        self.move.append(self.turnRight)
                        self.turnRight()
            # Check if front is end
            if self.checkAdj()[1]:
                self.currentIndex = self.checkAdj()[0]
                self.move.append(self.goForward)
        # Switching algorithm to Right Hand Rule
        elif algorithm == "Right Hand Rule":
            # Check if neighbor len == 0
            if len(self.maze.get_mapArr()[
                    self.currentIndex[0]][self.currentIndex[1]].neighbors) == 0:
                self.showturtle()
                self.state = False
                print("Invalid Maze")
                return False
            # Check if neighbor len == 4
            if len(self.maze.get_mapArr()[
                      self.currentIndex[0]][self.currentIndex[1]].neighbors) == 4:
                # While front is empty and not reach end
                while self.checkAdj()[0] and not self.checkAdj()[1]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj()[0], "make_path")
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj()[0]
            # While not reach end
            while not self.checkAdj()[1]:
                # Check if path has been walked over 3 times then break
                if len(self.seen) > 0 and self.seen.count(self.currentIndex) >= 3:
                    break
                # Get directions
                directionList = list(INDEX_MAP.keys())
                # checkRight wall index
                rightIndex = directionList[(directionList.index(
                    self.facing) - 1) % len(directionList)]
                # if front is end
                if self.checkAdj()[1]:
                    self.currentIndex = self.checkAdj()[0]
                    self.move.append(self.goForward)
                    break
                # if right is end and right is empty
                if self.checkAdj(rightIndex)[0] and self.checkAdj(rightIndex)[1]:
                    self.move.append(self.turnRight)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(rightIndex)[0]
                    self.turnRight()
                    break
                # If right is end
                if self.checkAdj(rightIndex)[0]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj(rightIndex)[0], "make_path")
                    self.move.append(self.turnRight)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(rightIndex)[0]
                    self.turnRight()
                else:
                    # checkFront wall is empty
                    if self.checkAdj()[0]:
                        self.seen.append(self.currentIndex)
                        self.colorCell(self.checkAdj()[0], "make_path")
                        self.move.append(self.goForward)
                        self.currentIndex = self.checkAdj()[0]
                    else:
                        self.move.append(self.turnLeft)
                        self.turnLeft()
            # Check if front is end
            if self.checkAdj()[1]:
                self.currentIndex = self.checkAdj()[0]
                self.move.append(self.goForward)
        elif algorithm == "Breadth First Search":
            # BFS Algorithm
            algo = BreadthFirstSearch(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        elif algorithm == "Depth First Search":
            # DFS Algorithm
            algo = DepthFirstSearch(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        elif algorithm == "A* Search":
            # A Star Algorithm
            algo = AStar(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        elif algorithm == "Greedy Best First Search":
            # GBFS Algorithm
            algo = Greedy(self)
            self.move = algo.start(
                self.maze.hashmap['start'][0], self.maze.hashmap['end'][0])
        # Switch to Free Roam
        elif algorithm == "Free Roam":
            # Set as free roam
            self.__roam = True
            self.pendown()
            self.showturtle()
            while self.state:
                directionList = list(INDEX_MAP.keys())
                # Arrows Key
                self.canvas.onkey(self.moveLeft, "Left")
                self.canvas.onkey(self.moveRight, "Right")
                self.canvas.onkey(self.moveForward, "Up")
                self.canvas.onkey(self.moveDown, "Down")
                if not self.state:
                    self.penup()
                    break
                # On key link to movement
                self.canvas.listen()
                self.canvas.mainloop()
        # Show Turtle
        self.showturtle()
        # Check if Left or Right Hand Algo
        if not self.__roam and algorithm in ["Left Hand Rule", "Right Hand Rule"]:
            # Reset turtle
            self.setheading(0)
            self.facing = DIRECTION_MAP[round(self.heading())]
            self.pendown()
            self.currentIndex = [int((self.maze.startY - self.y) /
                                     self.size), int((self.x - self.maze.endX)/self.size)]
            # Move turtle until end
            for steps in self.move:
                if not self.state:
                    break
                steps()
                time.sleep(0.01)
            # Check if not currently is at end of maze
            if not self.maze.get_mapArr()[
                    self.currentIndex[0]][self.currentIndex[1]].is_end():
                self.showturtle()
                self.state = False
                print("Invalid Maze")
                return False
            self.penup()
        elif not self.__roam and algorithm in ["Breadth First Search", "Depth First Search", "A* Search", "Greedy Best First Search"]:
            # Reset turtle
            self.setheading(0)
            self.facing = DIRECTION_MAP[round(self.heading())]
            self.currentIndex = [int((self.maze.startY - self.y) /
                                     self.size), int((self.x - self.maze.endX)/self.size)]
            path = self.move
            # Update path
            if path is None:
                self.showturtle()
                self.state = False
                self.penup()
                return False
            self.move = []
            currentBlock = path[-1]  # Initialise currentBlock as start
            # Loop through all path
            for idx, pathBlock in enumerate(path):
                if not self.state:
                    break
                if not pathBlock.is_start():
                    for [facing, index] in INDEX_MAP.items():
                        # Calculate facing and direction to move
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
                # Check if path block is end or start then dont color
                if pathBlock.is_end() or pathBlock.is_start():
                    continue
                pathBlock.make_path()
                pathBlock.draw()
                time.sleep(0.01)
            # Reset turtle
            self.setheading(0)
            self.facing = DIRECTION_MAP[round(self.heading())]
            self.pendown()
            self.currentIndex = [int((self.maze.startY - self.y) /
                                     self.size), int((self.x - self.maze.endX)/self.size)]
            # Loop through to move turtle
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
        self.maze.reset()
        self.size = self.maze.size
        if self.maze.hashmap['start']:
            self.update_pos(x=self.maze.hashmap['start'][0].x, y=self.maze.hashmap['start'][0].y)
        self.setpos(int(self.startX), int(self.startY))
        self.shapesize(self.size / 40)
        self.x = self.startX
        self.y = self.startY
        self.currentIndex = [int((self.maze.startY - self.y) /
                                 self.size), int((self.x - self.maze.endX)/self.size)]
        self.setheading(0)
        self.facing = DIRECTION_MAP[round(self.heading())]
        self.showturtle()
