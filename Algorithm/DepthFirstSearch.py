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

from Algorithm.BreadthFirstSearch import BreadthFirstSearch
from Algorithm.Stack import Stack

# Inherit BreadthFirstSearch
class DepthFirstSearch(BreadthFirstSearch):
    def __init__(self, character):
        # Super parent
        super().__init__(character)
        # Change frontier from Queue to Stack
        self.frontier = Stack()
