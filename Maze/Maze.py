import random
from Maze.Block import Block
from Maze.Pen import Pen

VALID_PATH = ["X", "s", "e", "."]


class Maze:
    def __init__(self,  canvas=None, size=40):
        self.size = size
        self.__mapArr = []
        self.canvas = canvas
        self.hashmap = {
            "building": [],
            "start": [],
            "end": [],
            "road": [],
        }
        self.state = False

    def upload_map(self, filePath):
        with open(filePath, 'r', encoding="utf8") as f:
            self.__mapString = f.read().strip()
            self.rows = len(self.__mapString.split("\n"))
            self.columns = len(self.__mapString.split("\n")[0])
            containsStart = False
            containsEnd = False
        # Ensure that the no of rows and columns are the same throughout
        for i in range(self.rows):
            if self.columns != len(self.__mapString.split("\n")[i]):
                return "Map have different row / column sizes"
            for j in range(self.columns):
                if self.__mapString.split("\n")[i][j] not in VALID_PATH:
                    return "Map have invalid character"
                elif self.__mapString.split("\n")[i][j] == "s":
                    if containsStart:
                        return "Multiple start found"
                    containsStart = True
                elif self.__mapString.split("\n")[i][j] == "e":
                    if containsEnd:
                        return "Multiple end found"
                    containsEnd = True
        self.size = min(48 - max(self.rows, self.columns), 40)
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

    def draw_map(self, canvas=None):
        if canvas == None:
            self.canvas = canvas
        pen = Pen(canvas=self.canvas, tile_size=self.size)
        self.pen = pen
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
        self.state = True
        for row in range(self.rows):
            currentY = startY - row * self.size
            rowArr = []
            for col in range(self.columns):
                currentX = endX + col * self.size
                blockType = list(
                    self.__mapString.split("\n")[row])[col]
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
                # pen.write(f"[{row}, {col}]", align="center")
            self.__mapArr.append(rowArr)
        for row in range(self.rows):
            for col in range(self.columns):
                self.__mapArr[row][col].update_neighbors(self.__mapArr)
        self.state = False
        return

    def saveFile(self, filePath):
        self.__generate_mapString()
        with open(filePath, "w") as f:
            f.write(self.__mapString)
            f.close()
        return


    def __generate_mapString(self):
        textArr = []
        for row in range(self.rows):
            rowArr = []
            for col in range(self.columns):
                cell = self.__mapArr[row][col]
                cellStr = ""
                if cell.is_wall():
                    cellStr = "X"
                elif cell.is_start():
                    cellStr = "s"
                elif cell.is_end():
                    cellStr = "e"    
                else:
                    cellStr = "."
                rowArr.append(cellStr)
            textArr.append("".join(rowArr))
        self.__mapString = "\n".join(textArr)
        return self.__mapString

    def generate_maze(self, rows, cols, canvas):
        self.columns = cols
        self.rows = rows
        self.canvas = canvas
        pen = Pen(canvas=canvas, tile_size=self.size)
        self.pen = pen
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
        self.state = True
        self.__mapArr = []
        for row in range(self.rows):
            currentY = startY - row * self.size
            rowArr = []
            for col in range(self.columns):
                currentX = endX + col * self.size
                rowArrBlock = Block(
                    row, col, self.size, self.rows, self.columns, canvas=self.canvas, x=currentX, y=currentY)
                rowArrBlock.make_wall()
                rowArr.append(rowArrBlock)
            self.__mapArr.append(rowArr)
        # startIndex = [random.randint(1, self.rows - 2), random.randint(1, self.columns - 2)]
        # startIndex = [1,1]
        # startBlock = self.__mapArr[startIndex[0]][startIndex[1]]
        # startBlock.reset()
        # self.__generate_mapString()
        # frontiers = []
        # frontiers.append(startBlock)
        # while len(frontiers) > 0:
        #     currentBlock = frontiers[random.randint(0, len(frontiers) - 1)]
        #     currentBlock.update_frontiers(self.__mapArr)
        #     frontierNeighbor = currentBlock.frontiers
        #     if len(frontierNeighbor) > 0:
        #         currentPath = frontierNeighbor[random.randint(0, len(frontierNeighbor) - 1)]
        #         if currentPath.row == currentBlock.row:
        #             print(currentBlock)
        #             print(currentPath)
        #             print(self.__mapArr[currentBlock.row][int((currentBlock.col + currentPath.col) / 2)])
        #             self.__mapArr[currentBlock.row][int((currentBlock.col + currentPath.col) / 2)].reset()
        #         elif currentPath.col == currentBlock.col:
        #             print(currentBlock)
        #             print(currentPath)
        #             print(
        #                 self.__mapArr[int((currentBlock.row + currentPath.row) / 2)][currentBlock.col])
        #             self.__mapArr[int((currentBlock.row + currentPath.row) / 2)][currentBlock.col].reset()
        #         currentPath.reset()
        #     currentBlock.reset()
        #     frontiers.remove(currentBlock)
        #     currentBlock = currentPath
        #     frontiers.append(currentPath)
        #     self.__generate_mapString()
        #     print("-" * 10)
        #     print(self.__mapString)
        # startBlock.make_start()
        # currentBlock.make_end()

        self.__generate_mapString()
        self.state = False
        # print("-" * 10)
        # print(self.__mapString)
        # print(self.__mapArr)
