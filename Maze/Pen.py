from turtle import RawTurtle

class Pen(RawTurtle):
    def __init__(self, tile_size=25, cursor_size = 20, canvas = None):
        super().__init__(canvas)
        self.shape('square')
        self.hideturtle()
        self.tile_size = tile_size
        self.cursor_size = cursor_size
        self.shapesize(tile_size / cursor_size)
        self.pencolor('black')
        self.penup()
        self.speed('fastest')

    def update_size(self, tile_size):
        self.tile_size = tile_size
        self.shapesize(self.tile_size / self.cursor_size)
        
