class Algorithm:
  def __init__(self, character):
    self.character = character
    
  # Abstract Functions
  def start(self):
    raise NotImplementedError("Subclass must implement abstract method") 
