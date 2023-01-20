from turtle import RawTurtle

class Pen(RawTurtle):
    def __init__(self, tile_size=25, cursor_size = 20, canvas = None):
        super().__init__(canvas)
        self.shape('square')
        self.shapesize(tile_size / cursor_size)
        self.pencolor('black')
        self.penup()
        self.speed('fastest')

class Trail(RawTurtle):
    def __init__(self, tile_size=25, cursor_size = 20, canvas = None):
        super().__init__(canvas)
        self.shape('square')
        self.shapesize(tile_size / cursor_size)
        
        self.speed('fastest')
