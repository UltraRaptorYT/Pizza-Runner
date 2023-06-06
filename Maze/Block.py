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

from Maze.Pen import Pen

# Create node which acts like a graph node ~ Hong Yu
class Block:
    def __init__(self, row, col, size, total_rows, total_cols, canvas, x=None, y=None):
        # Preset details
        self.row = row
        self.col = col
        self.x = x if x is not None else row * size
        self.y = y if y is not None else col * size
        self.color = "white"
        self.neighbors = []
        self.size = size
        self.total_rows = total_rows
        self.total_cols = total_cols
        self.canvas = canvas
        self.parent = None
        self.g_score = float('inf')
        self.f_score = float('inf')

    # Get position of block
    def get_pos(self):
        return self.row, self.col

    # Check if is reset
    def is_reset(self):
        return self.color == "white"

    # Check if is open
    def is_open(self):
        return self.color == "yellow"

    # Check if is path
    def is_path(self):
        return self.color == "orange"

    # Check if is wall
    def is_wall(self):
        return self.color == "grey"

    # Check if is start
    def is_start(self):
        return self.color == "lightgreen"

    # Check if is end
    def is_end(self):
        return self.color == "lightblue"

    # Reset color
    def reset(self):
        self.color = "white"

    # Set start color
    def make_start(self):
        self.color = "lightgreen"

    # Set open color
    def make_open(self):
        self.color = "yellow"

    # Set wall color
    def make_wall(self):
        self.color = "grey"

    # Set end color
    def make_end(self):
        self.color = "lightblue"

    # Set path color
    def make_path(self):
        self.color = "orange"

    # Draw/Color block
    def draw(self):
        try:
            self.pen.hideturtle()
        except AttributeError:
            self.pen = Pen(canvas=self.canvas, tile_size=self.size)
        self.pen.speed("fastest")
        self.pen.hideturtle()
        self.pen.fillcolor(self.color)
        self.pen.setpos(self.x, self.y)
        self.pen.stamp()
        return

    # Clear drawings
    def clear_stamps(self):
        try:
            self.pen.clearstamps()
        except AttributeError:
            return
        
    # Update neighbors [Connect them using edges and vertex]
    def update_neighbors(self, grid):
        self.neighbors = []
        # DOWN
        if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall():
            self.neighbors.append(grid[self.row + 1][self.col])

        # UP
        if self.row > 0 and not grid[self.row - 1][self.col].is_wall():
            self.neighbors.append(grid[self.row - 1][self.col])

        # RIGHT
        if self.col < self.total_cols - 1 and not grid[self.row][self.col + 1].is_wall():
            self.neighbors.append(grid[self.row][self.col + 1])

        # LEFT
        if self.col > 0 and not grid[self.row][self.col - 1].is_wall():
            self.neighbors.append(grid[self.row][self.col - 1])

    # Method overloading
    def __lt__(self, other):
        return False

    # Method overloading
    def __str__(self):
        return str([self.row, self.col])
