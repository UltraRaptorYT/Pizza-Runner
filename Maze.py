from Blocks.Block import Block
import turtle as t


class Maze:
    def __init__(self, tk, rows=8, columns=12):
        self.tk = tk
        self.rows = rows
        self.columns = columns
        self._map = [[Block() for x in range(columns)] for y in range(rows)]

    def set_map(self):
        print("hi")
        return

    def get_map(self):
        print(self._map)
        return

    def upload_map(self):
        return
    
    def draw(self, tk):
        for row in range(len(self._map)):
            for col in range(len(self._map[row])):   
                self._map[row][col].drawBlock(tk)
        return tk
