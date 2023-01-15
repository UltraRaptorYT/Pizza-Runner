from turtle import RawTurtle
import time

class Character(RawTurtle):
    def __init__(self,maze,canvas=None,x=0,y=0,size=40):
        super().__init__(canvas)
        self.hideturtle()
        self.shape('turtle')
        self.pencolor('black')
        self.penup()
        self.setpos(x,y)
        self.maze = maze
        self.showturtle()
        self.currentIndex = x
        self.size = size
        print(self.currentIndex)

    def start(self, algorithm = "Left Hand Rule"):
      startTime = 0
      self.algorithm = algorithm
      exploredNum = 0 # No. of explored path
      self.forward(self.size)
      print(self.algorithm)
      self.seen = []
      if algorithm == "Left Hand Rule":
          print(self.maze.mapArr)
          return
      return

    def print(self):
        print("Hi")
      
      
      
