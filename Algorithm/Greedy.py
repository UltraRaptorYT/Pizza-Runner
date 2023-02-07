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

from Algorithm.Algorithm import Algorithm
import time

# Inherit Algorithm
class Greedy(Algorithm):
  def __init__(self, character):
    # Super parent
    super().__init__(character)
    #Priority Queue
    self.frontier = []

  # Calculate heuristic [Manhattan Distance]
  def heuristic(self, node, end):
    return abs(node.row - end.row) + abs(node.col - end.col)

  # Returns node from the open list with the lowest f score
  def lowestFScore(self, openset):
    winner = openset[0]
    for nodes in openset:
      if nodes.f_score < winner.f_score:
        winner = nodes
    return winner
  
  # Overloading Abstraction Function
  def start(self, start, end):
    # Start priority queue
    self.frontier = [start]
    start.f_score = self.heuristic(start, end)
    # Check and ensure frontier > 0
    while len(self.frontier) > 0:
      currentGrid = self.lowestFScore(self.frontier)
      # Update neighbors
      currentGrid.update_neighbors(self.character.maze.get_mapArr())
      # Stop if state changes
      if not self.character.state:
            return
      # Check if it is the end
      if currentGrid.is_end():
        # Backtrack back to start position
        path = [currentGrid]
        while not (currentGrid.row == start.row and currentGrid.col == start.col):
          path.append(currentGrid.parent)
          currentGrid = currentGrid.parent
        return path
      # Color cell if not start
      if not currentGrid.is_start():
        currentGrid.make_open()
        currentGrid.draw()
      # Append frontier and seen
      self.frontier.remove(currentGrid)
      self.seen.append(currentGrid)
      # Loop through all neighbor
      for neighbor in currentGrid.neighbors:
        # Ignore if already checked
        if neighbor in self.seen:
          continue
        # Update g_score and f_score
        neighbor.f_score = self.heuristic(neighbor, end)
        self.frontier.append(neighbor)
        neighbor.parent = currentGrid
      time.sleep(0.01)
    # Invalid Maze
    if len(self.frontier) == 0:
      print("Invalid Maze")
    return
  

