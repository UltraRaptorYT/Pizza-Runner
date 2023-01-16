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
        self.currentIndex = [int((self.maze.startY - self.y) /
                             self.size), int((self.x - self.maze.endX)/self.size)]
        print(self.currentIndex)
        print(self.facing)

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
        print(self.currentIndex)
        print(self.maze.get_mapArr())
        if validPath:
            self.currentIndex = validPath
            self.forward(self.size)

    def checkAdj(self):
        movingIndex = list(self.currentIndex)
        movingIndex[0] += INDEX_MAP[self.facing][0]
        movingIndex[1] += INDEX_MAP[self.facing][1]
        checkTile = self.maze.get_mapArr()[movingIndex[0]][movingIndex[1]]
        if checkTile == "X":
            return [False, False]
        elif checkTile == "e":
            return [movingIndex, True]
        else:
            return [movingIndex, False]
    
    def start(self, algorithm="Left Hand Rule"):
        startTime = 0
        self.algorithm = algorithm
        exploredNum = 0  # No. of explored path
        print(self.algorithm)
        self.seen = []
        if algorithm == "Left Hand Rule":
            self.goForward()
            return
        return

    def print(self):
        self.goForward()
        print(self.maze)
