from Algorithm.Queue import Queue

class Algorithm:
  def __init__(self, character):
    self.character = character
    self.frontier = Queue()
    self.seen = []
    
  # Abstract Functions
  def start(self, start, end):
    raise NotImplementedError("Subclass must implement abstract method") 

