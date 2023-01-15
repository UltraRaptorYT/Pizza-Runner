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


class Button(RawTurtle):
    def __init__(self, canvas=None, x=0, y=0, text="", startShape="square", size=2, startColor="lightgreen", clickColor="green", clickFunc=None):
        super().__init__(canvas)
        self.canvas = canvas
        self.shapeSize = size
        self.x = x
        self.y = y
        self.startShape = startShape
        self.startColor = startColor
        self.clickColor = clickColor
        self.clickFunc = clickFunc
        self.text = text
        return

    def draw(self):
        self.speed('fastest')
        self.hideturtle()
        self.shapesize(self.shapeSize)
        self.shape(self.startShape)
        self.fillcolor(self.startColor)
        self.penup()
        self.goto(self.x, self.y)
        self.onclick(self.onClick)
        self.setheading(90)
        self.showturtle()
        self.write(self.text, align='center')

    def onClick(self, x, y):
        self.fillcolor(self.clickColor)
        self.write(self.text, align='center')
        if self.clickFunc != None:
            self.clickFunc()
        self.fillcolor(self.startColor)
        self.write(self.text, align='center')
        return
