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

class Text(RawTurtle):
    def __init__(self, text, canvas = None, font=None, bold="normal", fontSize=15,align="center",x=0,y=0):
        super().__init__(canvas)
        self.canvas = canvas
        self.fontSize = fontSize
        self.font = font
        self.bold = bold
        self.align = align
        self.x = x
        self.y = y
        self.text = text
        

    def draw(self):
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.setpos(self.x,self.y)
        self.write(self.text, font=(self.font,self.fontSize,self.bold),align=self.align)
