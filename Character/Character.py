from turtle import RawTurtle
import time

class Character(RawTurtle):
    def __init__(self,canvas=None,x=0,y=0):
        super().__init__(canvas)
        self.hideturtle()
        self.shape('turtle')
        self.pencolor('black')
        self.penup()
        self.setpos(x,y)
        self.showturtle()

    def start(self, algorithm = "Left Hand Rule"):
      startTime = 0
      self.algorithm = algorithm
      exploredNum = 0 # No. of explored path
      print(self.algorithm)
      self.seen = []
      if algorithm == "Breadth First Search":
          print("hi")
          return
      return
      
      
      
