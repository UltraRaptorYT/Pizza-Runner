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

# Inherit Algorithm ~ Hong Yu + Samuel
class BreadthFirstSearch(Algorithm):
  def __init__(self, character):
    # Super parent
    super().__init__(character)

  # Overloading Abstraction Function
  def start(self, start, end):
    # Start queue
    self.frontier.add(start)
    currentGrid = None
    # Check and ensure frontier > 0
    while not self.frontier.isEmpty():
      currentGrid = self.frontier.remove()  
      # Update neighbors    
      currentGrid.update_neighbors(self.character.maze.get_mapArr())
      # Stop if state changes
      if not self.character.state:
            return
      # Check if currentGrid exist in seen
      if currentGrid in self.seen:
        continue
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
      # Append seen
      self.seen.append(currentGrid)
      # Loop through all neighbor
      for neighbor in currentGrid.neighbors:
        # Ignore if already checked
        if neighbor in self.seen:
          continue
        # Update parent and append frontier to neighbors
        neighbor.parent = currentGrid
        self.frontier.add(neighbor)
      time.sleep(0.01) 
    # Invalid Maze
    if self.frontier.isEmpty():
      print("Invalid Maze")
    return
