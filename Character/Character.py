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
        self.facing = DIRECTION_MAP[self.heading()]
        self.startX = x
        self.startY = y
        self.currentIndex = [int((self.maze.startY - self.y) /
                             self.size), int((self.x - self.maze.endX)/self.size)]
        print(self.currentIndex)
        print(self.facing)
        self.state = False

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
            self.forward(self.size)
            self.step += 1
            time.sleep(0.1)

    def checkAdj(self, direction=None):
        if direction is None:
            direction = self.facing
        movingIndex = list(self.currentIndex)
        movingIndex[0] += INDEX_MAP[direction][0]
        movingIndex[1] += INDEX_MAP[direction][1]
        checkTile = self.maze.get_mapArr()[movingIndex[0]][movingIndex[1]]
        if checkTile == "X":
            return [False, False]
        elif checkTile == "e":
            return [movingIndex, True]
        else:
            return [movingIndex, False]
    
    def start(self, algorithm="Left Hand Rule"):
        if self.pos() != (self.startX, self.startY):
            self.reset_everything()
            time.sleep(0.5)
        startTime = 0
        self.step = 0
        self.algorithm = algorithm
        exploredNum = 0  # No. of explored path
        print(self.algorithm)
        self.seen = []
        self.state = True
        if algorithm == "Left Hand Rule":
            self.pendown()    
            while not self.checkAdj()[1] and self.step < 50:     
                directionList = list(INDEX_MAP.keys())  
                # checkLeft wall
                if self.checkAdj(directionList[(directionList.index(self.facing) + 1) % len(directionList)])[0]:
                    self.turnLeft()
                    self.goForward()    
                else:
                    # checkFront wall
                    if self.checkAdj()[0]:
                        self.goForward()
                    else:
                        self.turnRight()        
            self.goForward()
        self.state = False
        return

    def reset_everything(self):
        self.reset()
        self.hideturtle()
        self.penup()
        self.setpos(self.startX, self.startY)
        self.x = self.startX
        self.y = self.startY
        self.currentIndex = [int((self.maze.startY - self.y) /
                        self.size), int((self.x - self.maze.endX)/self.size)]
        self.setheading(0)
        self.maze.reset()
        self.showturtle()
        print(self.currentIndex)
