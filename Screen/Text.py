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

# Inherit RawTurtle
class Text(RawTurtle):
    def __init__(self, text, canvas = None, font=None, bold="normal", fontSize=15,align="center",x=0,y=0):
        # Super parent
        super().__init__(canvas)
        # Setup
        self.canvas = canvas
        self.fontSize = fontSize
        self.font = font
        self.bold = bold
        self.align = align
        self.x = x
        self.y = y
        # Set text to private to prevent text alteration
        self.__text = text
        self.hideturtle()

    # Draw text for visualisation
    def draw(self):
        self.hideturtle()
        self.penup()
        self.speed('fastest')
        self.setpos(self.x,self.y)
        self.write(self.__text, font=(self.font,self.fontSize,self.bold),align=self.align)

    # Private Setter function
    def __setText(self, text):
        self.__text = text

    # Getter Function
    def getText(self):
        return self.__text

    # Public setter function to modify text and re render
    def changeText(self, text):
        self.__setText(text)
        self.clear()
        self.draw()
