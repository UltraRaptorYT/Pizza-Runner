from Maze.Pen import Pen
import turtle as t


class Maze:
    def __init__(self,  mapString=None, size=40):
        self.size = size
        self.__mapArr = []
        self.mapString = mapString
        self.hashmap = {
            "wall": [],
            "start": [],
            "end": [],
            "path": [],
        }

    def upload_map(self, filePath):
        with open(filePath, 'r', encoding="utf8") as f:
            self.mapString = f.read().strip()                
            self.rows = len(self.mapString.split("\n"))
            self.columns = len(self.mapString.split("\n")[0])
        # Ensure that the no of rows and columns are the same throughout
        for i in range(1, self.rows):
            if self.columns != len(self.mapString.split("\n")[i]):
                return True
        return False

    def get_mapArr(self):
        return self.__mapArr

    def reset(self, canvas):
        canvas.delete("all")
        self.draw_map(canvas)
        return

    def draw_map(self, canvas):
        pen = Pen(canvas=canvas, tile_size=self.size)
        endX = -(self.columns * self.size / 2)
        startY = self.rows * self.size / 2
        self.endX = endX
        self.startY = startY
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
                    print(row,col)
                elif blockType == 'e':
                    pen.fillcolor("lightblue")
                    self.hashmap["end"].append((currentX, currentY))
                else:
                    pen.fillcolor("white")
                    self.hashmap["path"].append((currentX, currentY))
                pen.setpos(currentX, currentY)
                pen.stamp()
            self.__mapArr.append(rowArr)
        return
