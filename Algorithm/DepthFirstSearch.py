from Algorithm.BreadthFirstSearch import BreadthFirstSearch
from Algorithm.Stack import Stack

class DepthFirstSearch(BreadthFirstSearch):
    def __init__(self, character):
        super().__init__(character)
        self.frontier = Stack()
