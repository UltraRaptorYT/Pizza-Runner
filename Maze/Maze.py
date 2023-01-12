from Maze.Pen import Pen
import turtle as t


class Maze:
    def __init__(self,  rows=8, columns=12, size=40):
        self.rows = rows
        self.columns = columns
        self.size = size
        self.mapArr = []
        self.mapString = """XXXXXXXXXXXX
X...X..X..eX
X.X....X.XXX
X..X.X.X.X.X
XX.XXX.X...X
X........X.X
XsXX...X...X
XXXXXXXXXXXX"""
        self.hashmap = {
            "wall": [],
            "start": [],
            "end": [],
            "path": [],
        }

    # def set_map(self):
    #     print("hi")
    #     return

    # def get_map(self):
    #     print(self._map)
    #     return

    def upload_map(self, mapString="""XXXXXXXXXXXX
X...X..X..eX
X.X....X.XXX
X..X.X.X.X.X
XX.XXX.X...X
X........X.X
XsXX...X...X
XXXXXXXXXXXX"""):
        # ! Input need to ensure that no of rows and columns are the same throughout
        self.mapString = mapString
        self.rows = len(self.mapString.split("\n"))
        self.columns = len(self.mapString.split("\n")[0])
        return

    def reset(self, canvas):
        canvas.delete("all")
        self.draw(canvas)
        return

    def draw(self, canvas):
        pen = Pen(canvas=canvas, tile_size=self.size)
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        for row in range(self.rows):
            currentY = startY - row * self.size
            rowArr = []
            for col in range(self.columns):
                currentX = endX + col * self.size
                blockType = list(
                    self.mapString.split("\n")[row])[col]
                rowArr.append(blockType)
                if blockType == 'X':
                    pen.fillcolor("grey")
                    self.hashmap["wall"].append((currentX, currentY))
                elif blockType == 's':
                    pen.fillcolor("lightgreen")
                    self.hashmap["start"].append((currentX, currentY))
                elif blockType == 'e':
                    pen.fillcolor("lightblue")
                    self.hashmap["end"].append((currentX, currentY))
                else:
                    pen.fillcolor("white")
                    self.hashmap["path"].append((currentX, currentY))
                pen.setpos(currentX, currentY)
                pen.stamp()
            self.mapArr.append(rowArr)
        return
