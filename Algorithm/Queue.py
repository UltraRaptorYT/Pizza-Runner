class Queue:
  def __init__(self):
    self.frontier = []

  def isEmpty(self):
    return len(self.frontier) == 0

  def add(self, grid):
    self.frontier.append(grid)

  def remove(self):
    return self.frontier.pop(0)

  def contains(self, grid):
    return any(element.row == grid.row and element.col == grid.col for element in self.frontier)
