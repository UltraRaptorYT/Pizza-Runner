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

# Inherit Raw Turtle
class Pen(RawTurtle):
    def __init__(self, tile_size=25, cursor_size = 20, canvas = None):
        super().__init__(canvas)
        # Setup Pen
        self.shape('square')
        self.hideturtle()
        self.tile_size = tile_size
        self.cursor_size = cursor_size
        self.shapesize(tile_size / cursor_size)
        self.pencolor('black')
        self.penup()
        self.speed('fastest')

    # Due to custom sizing, we need to update the size of the pen
    def update_size(self, tile_size):
        self.tile_size = tile_size
        self.shapesize(self.tile_size / self.cursor_size)
        
