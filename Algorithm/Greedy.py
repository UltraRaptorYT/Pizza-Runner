from Algorithm.Algorithm import Algorithm
import time
class Greedy(Algorithm):
  def __init__(self, character):
    super().__init__(character)
    self.frontier = []

  def heuristic(self, node, end):
    return abs(node.row - end.row) + abs(node.col - end.col)
  
  def lowestFScore(self, openset):
    winner = openset[0]
    for nodes in openset:
      if nodes.f_score < winner.f_score:
        winner = nodes
    return winner
  
  # Overloading Abstraction Function
  def start(self, start, end):
    self.frontier = [start]
    start.f_score = self.heuristic(start, end)
    while len(self.frontier) > 0:
      currentGrid = self.lowestFScore(self.frontier)
      currentGrid.update_neighbors(self.character.maze.get_mapArr())
      if not self.character.state:
            return
      if currentGrid.is_end(): # Code this later
        path = [currentGrid]
        while not (currentGrid.row == start.row and currentGrid.col == start.col):
          path.append(currentGrid.parent)
          currentGrid = currentGrid.parent
        return path
      if not currentGrid.is_start():
        currentGrid.make_open()
        currentGrid.draw()
      self.frontier.remove(currentGrid)
      self.seen.append(currentGrid)
      for neighbor in currentGrid.neighbors:
        if neighbor in self.seen:
          continue
        neighbor.f_score = self.heuristic(neighbor, end)
        self.frontier.append(neighbor)
        neighbor.parent = currentGrid
      time.sleep(0.01)
    if len(self.frontier) == 0:
      print("Invalid Maze")
    return
  
  