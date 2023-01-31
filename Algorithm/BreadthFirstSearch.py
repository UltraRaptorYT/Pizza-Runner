from Algorithm.Algorithm import Algorithm
import time
class BreadthFirstSearch(Algorithm):
  def __init__(self, character):
    super().__init__(character)

  # Overloading Abstraction Function
  def start(self, start, end):
    self.frontier.add(start)
    currentGrid = None
    while not self.frontier.isEmpty():
      currentGrid = self.frontier.remove()
      # print(currentGrid.row, currentGrid.col)
      if currentGrid.row == 5 and currentGrid.col == 7:
        print(currentGrid.neighbors)
        for neighbor in currentGrid.neighbors:
          print(neighbor.row, neighbor.col)
      if currentGrid in self.seen:
        # print("in seen")
        continue
      if currentGrid.is_end(): # Code this later
        path = [currentGrid]
        while not (currentGrid.row == start.row and currentGrid.col == start.col):
          path.append(currentGrid.parent)
          currentGrid = currentGrid.parent
        return path
      if not currentGrid.is_start():
        currentGrid.make_open()
        currentGrid.draw()
      self.seen.append(currentGrid)
      for neighbor in currentGrid.neighbors:
        if neighbor in self.seen:
          continue
        neighbor.parent = currentGrid
        self.frontier.add(neighbor)
      time.sleep(0.01) 
    if self.frontier.isEmpty():
      print("Invalid Maze")
    return
