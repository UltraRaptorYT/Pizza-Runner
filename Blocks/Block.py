import turtle as t

class Block:
    def __init__(self, x=0, y=0, size=10):
        self.x = x
        self.y = y
        self.size = size
        pass

    def drawBlock(self, turtle):
        turtle.goto(self.x, self.y)
        turtle.pendown()
        turtle.begin_fill()
        for i in range(4):
            turtle.forward(self.size)
            turtle.right(90)
        turtle.end_fill()
        turtle.penup()
        return
