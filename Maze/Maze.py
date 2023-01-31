from Maze.Block import Block
from Maze.Pen import Pen

VALID_PATH = ["X", "s", "e", "."]


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
            containsStart = False
            containsEnd = False
        # Ensure that the no of rows and columns are the same throughout
        for i in range(self.rows):
            if self.columns != len(self.mapString.split("\n")[i]):
                return "Map have different row / column sizes"
            for j in range(self.columns):
                if self.mapString.split("\n")[i][j] not in VALID_PATH:
                    return "Map have invalid character"
                elif self.mapString.split("\n")[i][j] == "s":
                    if containsStart:
                        return "Multiple start found"
                    containsStart = True
                elif self.mapString.split("\n")[i][j] == "e":
                    if containsEnd:
                        return "Multiple end found"
                    containsEnd = True
        self.size = min(48 - max(self.rows, self.columns), 40)
        print(self.size)
        if not containsStart:
            return "Missing start point"
        if not containsEnd:
            return "Missing end point"
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
                rowArrBlock = Block(
                    row, col, self.size, self.rows, self.columns, canvas=self.canvas, x=currentX, y=currentY)
                if blockType == 'X':
                    pen.fillcolor("grey")
                    rowArrBlock.make_wall()
                    self.hashmap["building"].append(rowArrBlock)
                elif blockType == 's':
                    pen.fillcolor("lightgreen")
                    rowArrBlock.make_start()
                    self.hashmap["start"].append(rowArrBlock)
                elif blockType == 'e':
                    pen.fillcolor("lightblue")
                    rowArrBlock.make_end()
                    self.hashmap["end"].append(rowArrBlock)
                else:
                    pen.fillcolor("white")
                    self.hashmap["road"].append(rowArrBlock)
                rowArr.append(rowArrBlock)
                pen.setpos(currentX, currentY)
                pen.stamp()
                pen.write(f"[{row}, {col}]", align="center")
            self.__mapArr.append(rowArr)
        for row in range(self.rows):
            for col in range(self.columns):
                self.__mapArr[row][col].update_neighbors(self.__mapArr)
        print("hi")
        self.state = False
        return
