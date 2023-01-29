from Maze.Pen import Pen

class Block:
  def __init__(self, row, col, size, total_rows, canvas, x=None, y=None):
    self.row = row
    self.col = col
    self.x = x if x is not None else row * size
    self.y = y if y is not None else col * size
    self.color = "white"
    self.neighbors = []
    self.size = size
    self.total_rows = total_rows
    self.canvas = canvas

  def get_pos(self):
    return self.row, self.col

  def is_closed(self):
    return self.color == "red"

  def is_open(self):
    return self.color == "yellow"

  def is_wall(self):
    return self.color == "grey"

  def is_start(self):
    return self.color == "lightgreen"

  def is_end(self):
    return self.color == "lightblue"

  def reset(self):
    self.color = "white"

  def make_start(self):
    self.color = "lightgreen"

  def make_closed(self):
    self.color = "red"

  def make_open(self):
    self.color = "yellow"

  def make_wall(self):
    self.color = "grey"

  def make_end(self):
    self.color = "lightblue"

  def make_path(self):
    self.color = "orange"

  def draw(self):
    pen = Pen(canvas=self.canvas, tile_size=self.size)
    pen.speed("fastest")
    pen.hideturtle()
    pen.fillcolor(self.color)
    pen.setpos(self.x, self.y)
    pen.stamp()
    return

  def update_neighbors(self, grid):
    self.neighbors = []
    if self.row < self.total_rows - 1 and not grid[self.row + 1][self.col].is_wall(): # DOWN
      self.neighbors.append(grid[self.row + 1][self.col])

    if self.row > 0 and not grid[self.row - 1][self.col].is_wall(): # UP
      self.neighbors.append(grid[self.row - 1][self.col])

    if self.col < self.total_rows - 1 and not grid[self.row][self.col + 1].is_wall(): # RIGHT
      self.neighbors.append(grid[self.row][self.col + 1])

    if self.col > 0 and not grid[self.row][self.col - 1].is_wall(): # LEFT
      self.neighbors.append(grid[self.row][self.col - 1])

  def __lt__(self, other):
    return False