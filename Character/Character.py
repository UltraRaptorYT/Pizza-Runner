from turtle import RawTurtle
import time

DIRECTION_MAP = {
    0: "EAST",
    90: "NORTH",
    180: "WEST",
    270: "SOUTH"
}

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
        print(self.currentIndex)
        print(self.facing)
        self.state = False
        self.step = 0
    
    # Basic Functions for algorithms
    def turnLeft(self):
        self.left(90)
        self.facing = DIRECTION_MAP[self.heading()]
        print(self.facing)

    def turnRight(self):
        self.right(90)
        self.facing = DIRECTION_MAP[self.heading()]
        print(self.facing)
    
    def goForward(self):
        validPath, isEnd = self.checkAdj()
        if isEnd:
            print("End")
        if validPath:
            self.currentIndex = validPath
            self.step += 1
            self.forward(self.size)

    #Basic movement for Free Roam
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
        # for neighbors in checkTile.neighbors:
        #     neighbors.make_open()
        #     neighbors.draw()
        if checkTile.is_wall():
            return [False, False]
        elif checkTile.is_end():
            return [movingIndex, True]
        else:
            # movingIndex
            return [movingIndex, False]

    def updateState(self, newState = None):
        print(self.state)
        if not newState is None:
            self.state = newState
        else:
            self.state = not self.state
        return self.state

    def colorCell(self, index):
        block = self.maze.get_mapArr()[index[0]][index[1]]
        if not block.is_wall():
            block.make_open()
            block.draw()
    
    # Start button setting the default algorithm to Left Hand Rule
    def start(self, algorithm="Left Hand Rule"):
        if self.pos() != (self.startX, self.startY):
            self.reset_everything()
            time.sleep(0.5)
        self.shapesize(self.size / 40)
        self.step = 0
        self.algorithm = algorithm
        exploredNum = 0  # No. of explored path
        print(self.algorithm)
        self.seen = []
        self.state = True
        self.move = []
        self.__roam = False
        print(self.currentIndex)
        if algorithm == "Left Hand Rule":
            while not self.checkAdj()[1]: 
                if len(self.seen) > 0 and self.currentIndex == [int((self.maze.startY - self.y) /
                                                                    self.size), int((self.x - self.maze.endX)/self.size)]:
                    break
                directionList = list(INDEX_MAP.keys())  
                # checkLeft wall
                leftIndex = directionList[(directionList.index(self.facing) + 1) % len(directionList)]
                if self.checkAdj(leftIndex)[0]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj(leftIndex)[0])                    
                    self.move.append(self.turnLeft)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(leftIndex)[0]
                    self.turnLeft()        
                else:
                    # checkFront wall
                    if self.checkAdj()[0]:
                        self.seen.append(self.currentIndex)
                        self.colorCell(self.checkAdj()[0])
                        self.move.append(self.goForward)
                        self.currentIndex = self.checkAdj()[0]
                    else:
                        self.move.append(self.turnRight)
                        self.turnRight()
            if self.checkAdj()[1]:
                self.move.append(self.goForward)
        # Switching algorithm to Right Hand Rule
        elif algorithm == "Right Hand Rule":
            while not self.checkAdj()[1]:
                if len(self.seen) > 0 and self.currentIndex == [int((self.maze.startY - self.y) /
                                                                    self.size), int((self.x - self.maze.endX)/self.size)]:
                    break
                directionList = list(INDEX_MAP.keys())
                # checkRight wall
                rightIndex = directionList[(directionList.index(
                    self.facing) - 1) % len(directionList)]
                if self.checkAdj(rightIndex)[0]:
                    self.seen.append(self.currentIndex)
                    self.colorCell(self.checkAdj(rightIndex)[0])
                    self.move.append(self.turnRight)
                    self.move.append(self.goForward)
                    self.currentIndex = self.checkAdj(rightIndex)[0]
                    self.turnRight()
                else:
                    # checkFront wall
                    if self.checkAdj()[0]:
                        self.seen.append(self.currentIndex)
                        self.colorCell(self.checkAdj()[0])
                        self.move.append(self.goForward)
                        self.currentIndex = self.checkAdj()[0]
                    else:
                        self.move.append(self.turnLeft)
                        self.turnLeft()
            if self.checkAdj()[1]:
                self.move.append(self.goForward)
        # if algorithm == "Breadth First Search":
        #     self.pendown()
        #     while not self.checkAdj()[1] and self.step < 50:
        #         directionList = list(INDEX_MAP.keys())
        #         #checkRight wall
        #         if self.checkAdj(directionList[(directionList.index(self.facing) - 1) % len(directionList)])[0] and self.checkAdj(directionList[(directionList.index(self.facing) + 1) % len(directionList)])[0]:
        #             self.turnRight()
        #             self.goForward()  
        #         #checkLeft wall
        #         if self.checkAdj(directionList[(directionList.index(self.facing) + 1) % len(directionList)])[0]:
        #             self.turnLeft()
        #             self.goForward()
        #         if self.checkAdj()[0]:
        #             self.goForward()
        #     self.goForward()
        # Switch to Free Roam
        elif algorithm == "Free Roam":
            self.__roam = True
            self.pendown()
            while not self.maze.get_mapArr()[self.currentIndex[0]][self.currentIndex[1]].is_end():     
                print(self.maze.get_mapArr()[
                      self.currentIndex[0]][self.currentIndex[1]].is_end())
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
                    break
                self.canvas.listen()
                self.canvas.mainloop()
        if not self.__roam:
            self.setheading(0)
            self.facing = DIRECTION_MAP[self.heading()]
            self.pendown()
            self.currentIndex = [int((self.maze.startY - self.y) /
                        self.size), int((self.x - self.maze.endX)/self.size)]
            for steps in self.move:
                steps()
            self.penup()
        self.state = False
        return
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
        print(self.currentIndex)

