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

# Create Queue class
# As Queue is FIFO, add and remove is based on append() and pop(0)
class Queue:
  def __init__(self):
    self.frontier = []

  # Check empty
  def isEmpty(self):
    return len(self.frontier) == 0

  # Append to frontier
  def add(self, grid):
    self.frontier.append(grid)

  # Remove from frontier
  def remove(self):
    return self.frontier.pop(0)

  # Check if same
  def contains(self, grid):
    return any(element.row == grid.row and element.col == grid.col for element in self.frontier)

  # Method overloading
  def __str__(self):
    queueString = "["
    for i in self.frontier:
      queueString += str(i) + ","
    queueString = queueString[:-1]
    queueString += "]"
    return queueString
