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

from Algorithm.Queue import Queue

# Inherit Queue ~ Hong Yu + Samuel
class Stack(Queue):
  def __init__(self):
    # Super parent
    super().__init__()

  # Method overloading
  def remove(self):
    return self.frontier.pop()
