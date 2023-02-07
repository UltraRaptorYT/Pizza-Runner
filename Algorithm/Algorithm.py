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

# Import Queue 
from Algorithm.Queue import Queue

# Create Abstract class
class Algorithm:
  def __init__(self, character):
    self.character = character
    self.frontier = Queue()
    self.seen = []
    
  # Abstract Functions
  def start(self, start, end):
    raise NotImplementedError("Subclass must implement abstract method") 

