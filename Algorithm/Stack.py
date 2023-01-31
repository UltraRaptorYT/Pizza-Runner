from Algorithm.Queue import Queue

class Stack(Queue):
  def __init__(self):
    super().__init__()

  def remove(self):
    return self.frontier.pop()
