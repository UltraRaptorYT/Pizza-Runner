from Maze.Pen import Pen
import turtle as t
import networkx as nx

VALID_PATH = ["X","s","e","."]
G = nx.Graph()

class Maze:
    def __init__(self,  mapString=None, size=40):
        self.size = size
        self.__mapArr = []
        self.mapString = mapString
        self.hashmap = {
            "building": [],
            "start": [],
            "end": [],
            "road": [],
        }
        self.state = False

    def upload_map(self, filePath):
        with open(filePath, 'r', encoding="utf8") as f:
            self.mapString = f.read().strip()                
            self.rows = len(self.mapString.split("\n"))
            self.columns = len(self.mapString.split("\n")[0])
        # Ensure that the no of rows and columns are the same throughout
        for i in range(self.rows):
            if self.columns != len(self.mapString.split("\n")[i]):
                return True
            for j in range(self.columns):
                if self.mapString.split("\n")[i][j] not in VALID_PATH:
                    return True
        return False

    def get_mapArr(self):
        return self.__mapArr

    def reset(self):
        self.pen.clearstamps()
        self.draw_map(self.canvas)
        return

    def draw_map(self, canvas):
        self.canvas = canvas
        pen = Pen(canvas=canvas, tile_size=self.size)
        self.pen = pen
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
        for row in range(self.rows):
            currentY = startY - row * self.size
            rowArr = []
            for col in range(self.columns):
                self.state = True
                currentX = endX + col * self.size
                blockType = list(
                    self.mapString.split("\n")[row])[col]
                rowArr.append(blockType)
                if blockType == 'X':
                    pen.fillcolor("grey")
                    self.hashmap["building"].append((currentX, currentY))
                    G.add_node((row, col), type='building')
                elif blockType == 's':
                    pen.fillcolor("lightgreen")
                    self.hashmap["start"].append((currentX, currentY))
                    print(row,col)
                elif blockType == 'e':
                    pen.fillcolor("lightblue")
                    self.hashmap["end"].append((currentX, currentY))
                else:
                    pen.fillcolor("white")
                    self.hashmap["road"].append((currentX, currentY))
                pen.setpos(currentX, currentY)
                pen.stamp()
            self.__mapArr.append(rowArr)
        self.state = False
        return
