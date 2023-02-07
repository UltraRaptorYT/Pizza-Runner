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

import random
from Maze.Block import Block
from Maze.Pen import Pen

# Set valid path type
VALID_PATH = ["X", "s", "e", "."]

# Create Maze class
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
        pen = Pen(canvas=self.canvas, tile_size=self.size)
        self.pen = pen
        self.state = False

    # Upload map from filepath
    def upload_map(self, filePath):
        # Read filepath and get result
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
                # Check for start and end and if there are duplicate
                elif self.__mapString.split("\n")[i][j] == "s":
                    if containsStart:
                        return "Multiple start found"
                    containsStart = True
                elif self.__mapString.split("\n")[i][j] == "e":
                    if containsEnd:
                        return "Multiple end found"
                    containsEnd = True
        # Formula to adjust size of map
        self.size = min(48 - max(self.rows, self.columns), 40)
        self.pen.update_size(self.size)
        # Missing points
        if not containsStart:
            return "Missing start point"
        if not containsEnd:
            return "Missing end point"
        return False

    # Getter for private self.__mapArr
    def get_mapArr(self):
        return self.__mapArr

    # Reset map
    def reset(self):
        self.pen.clearstamps()
        self.generate_mapString()
        for row in range(self.rows):
            for col in range(self.columns):
                if self.__mapArr[row][col].is_open() or self.__mapArr[row][col].is_path():
                    self.__mapArr[row][col].reset()
                    self.__mapArr[row][col].clear_stamps()
        self.draw_map(self.canvas)
        return

    # Draw Map
    def draw_map(self, canvas=None):
        # Restore hash
        self.hashmap["building"] = []
        self.hashmap["start"] = []
        self.hashmap["end"] = []
        self.hashmap["road"] = []
        if canvas == None:
            self.canvas = canvas
        # Reset map
        self.size = min(48 - max(self.rows, self.columns), 40)
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
        self.state = True
        # Loop through mapString
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
                    self.pen.fillcolor("grey")
                    rowArrBlock.make_wall()
                    self.hashmap["building"].append(rowArrBlock)
                elif blockType == 's':
                    self.pen.fillcolor("lightgreen")
                    rowArrBlock.make_start()
                    self.hashmap["start"].append(rowArrBlock)
                elif blockType == 'e':
                    self.pen.fillcolor("lightblue")
                    rowArrBlock.make_end()
                    self.hashmap["end"].append(rowArrBlock)
                else:
                    self.pen.fillcolor("white")
                    self.hashmap["road"].append(rowArrBlock)
                    rowArrBlock.reset()
                rowArr.append(rowArrBlock)
                self.pen.setpos(currentX, currentY)
                self.pen.stamp()
            self.__mapArr.append(rowArr)
        # Update the neighbors
        for row in range(self.rows):
            for col in range(self.columns):
                self.__mapArr[row][col].update_neighbors(self.__mapArr)
        self.state = False
        return

    # Save file function
    def saveFile(self, filePath):
        self.generate_mapString()
        with open(filePath, "w") as f:
            f.write(self.__mapString)
            f.close()
        return

    # Generate map string from map array
    def generate_mapString(self):
        textArr = []
        # Check individual cells
        for row in range(self.rows):
            rowArr = []
            for col in range(self.columns):
                cell = self.__mapArr[row][col]
                self.__mapArr[row][col].update_neighbors(self.__mapArr)
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
        # Concatenate to form mapString
        self.__mapString = "\n".join(textArr)
        self.size = min(48 - max(self.rows, self.columns), 40)
        self.pen.update_size(self.size)
        return self.__mapString

    # Soh Hong Yu's Additional Feature - generate maze
    def generate_maze(self, rows, cols, canvas):
        # Reset maps
        try:       
            for row in range(self.rows):
                for col in range(self.columns):
                    self.__mapArr[row][col].clear_stamps()
        except AttributeError:
            pass
        self.columns = cols
        self.rows = rows
        self.canvas = canvas
        self.size = min(48 - max(self.rows, self.columns), 40)
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
        self.state = True
        self.__mapArr = []
        visited = []
        for row in range(self.rows):
            currentY = startY - row * self.size
            rowArr = []
            visitedArr = []
            for col in range(self.columns):
                currentX = endX + col * self.size
                rowArrBlock = Block(
                    row, col, self.size, self.rows, self.columns, canvas=self.canvas, x=currentX, y=currentY)
                rowArrBlock.make_wall()
                rowArr.append(rowArrBlock)
                visitedArr.append(False)
            self.__mapArr.append(rowArr)
            visited.append(visitedArr)
        # Randomly choose r,c index
        r = random.randint(0, self.rows - 1)
        while r % 2 == 0:
            r = random.randint(0, self.rows - 1)
        c = random.randint(0, self.columns - 1)
        while c % 2 == 0:
            c = random.randint(0, self.columns - 1)

        # Inside function 
        def randomized_prim(r, c):
            currentBlock = self.__mapArr[r][c]
            visited[r][c] = True
            currentBlock.reset()
            directions = [(2, 0), (0, 2), (-2, 0), (0, -2)]
            random.shuffle(directions)
            # Recursive Backtracking method of maze generation
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if nr < 1 or nr > self.rows - 2 or nc < 1 or nc > self.columns - 2 or visited[nr][nc]:
                    continue
                else:
                    self.__mapArr[nr][nc].reset()
                    self.__mapArr[int((r + nr) / 2)][int((c + nc) / 2)].reset()
                    randomized_prim(nr, nc)
        # Make and set all maze array
        startBlock = self.__mapArr[r][c]
        randomized_prim(r, c)
        startBlock.make_start()
        # Reset hashmap
        self.hashmap["start"] = [startBlock]
        endRow = random.randint(1, self.rows - 2)
        endCol = random.randint(1, self.columns - 2)
        endBlock = self.__mapArr[endRow][endCol]
        # Randomly choose endBlock and check if endBlock spot has been taken
        while endBlock.is_start() or endBlock.is_wall():
            endRow = random.randint(1, self.rows - 2)
            endCol = random.randint(1, self.columns - 2)
            endBlock = self.__mapArr[endRow][endCol]
        endBlock.make_end()
        self.hashmap["end"] = [endBlock]
        self.generate_mapString()

    # Soh Hong Yu's Additional Features - Custom Map
    def custom_map(self, rows, cols, canvas):
        # Reset maps
        try:       
            for row in range(self.rows):
                for col in range(self.columns):
                    self.__mapArr[row][col].clear_stamps()
        except AttributeError:
            pass
        self.columns = cols
        self.rows = rows
        self.canvas = canvas
        self.size = min(48 - max(self.rows, self.columns), 40)
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
        self.state = True
        self.__mapArr = []
        # Re create mapArr
        for row in range(self.rows):
            currentY = startY - row * self.size
            rowArr = []
            for col in range(self.columns):
                currentX = endX + col * self.size
                rowArrBlock = Block(
                    row, col, self.size, self.rows, self.columns, canvas=self.canvas, x=currentX, y=currentY)
                rowArrBlock.make_open()
                rowArr.append(rowArrBlock)
            self.__mapArr.append(rowArr)
        self.generate_mapString()
        return
