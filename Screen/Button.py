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

# Inherit RawTurtle ~ Hong Yu
class Button(RawTurtle):
    def __init__(self, canvas=None, x=0, y=0, text="", startShape="square", size=2, startColor="lightgreen", clickColor="green", clickFunc=None, clickText=None, toggle=False, toggleFunc=None):
        super().__init__(canvas)
        # Setup button
        self.canvas = canvas
        self.shapeSize = size
        self.x = x
        self.y = y
        self.startShape = startShape
        self.startColor = startColor
        self.clickColor = clickColor
        self.clickFunc = clickFunc
        self.text = text
        self.toggle = toggle
        # Make if button is toggleable
        if self.toggle:
            self.toggleState = False
            self.toggleFunc = toggleFunc
        if clickText:
            self.clickText = clickText
        else:
            self.clickText = self.text
        self.hideturtle()
        return

    # Draw and create a new instance of button
    def draw(self):
        # Setup
        self.hideturtle()
        self.speed('fastest')
        self.shapesize(self.shapeSize)
        self.shape(self.startShape)
        self.fillcolor(self.startColor)
        self.penup()
        self.goto(self.x, self.y)
        self.onclick(self.onClick)
        self.setheading(90)
        self.showturtle()
        self.clear()
        self.write(self.text, align='center')
        # Modify state
        if self.toggle:
            if self.toggleState:
                self.fillcolor(self.clickColor)
                self.clear()
                self.write(self.clickText, align='center')
            else:
                self.fillcolor(self.startColor)
                self.clear()
                self.write(self.text, align='center')    

    # Update state of button
    def updateState(self):
        if self.toggleState:
            self.fillcolor(self.clickColor)
            self.clear()
            self.write(self.clickText, align='center')
        else:
            self.fillcolor(self.startColor)
            self.clear()
            self.write(self.text, align='center')    

    # Handle onclick of button
    def onClick(self, x, y):
        self.fillcolor(self.clickColor)
        self.clear()
        # Check if toggleable
        if self.toggle:
            self.toggleState = not self.toggleState
            if self.toggleState:
                self.fillcolor(self.clickColor)
                self.clear()
                self.write(self.clickText, align='center')
                if self.clickFunc != None:
                    self.clickFunc()
            else:
                self.fillcolor(self.startColor)
                self.clear()
                self.write(self.text, align='center')  
                if self.toggleFunc != None:
                    self.toggleFunc()
        else:
            self.write(self.clickText, align='center')
            if self.clickFunc != None:
                self.clickFunc()
            self.reset()
        return

    # Reset button
    def reset(self):
        self.fillcolor(self.startColor)
        self.clear()
        self.write(self.text, align='center')
        return
