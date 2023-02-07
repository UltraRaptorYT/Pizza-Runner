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

import sys
import os
import turtle as t
from Maze.Maze import Maze
from Character.Character import Character
from Screen.Text import Text
from Screen.Button import Button
from datetime import datetime, timedelta

ALGO_LIST = ["Left Hand Rule", "Right Hand Rule", "Breadth First Search",
             "Depth First Search", "A* Search", "Greedy Best First Search", "Free Roam"]

ALGO_INFO = {
    "Left Hand Rule": "The 'Left Hand Rule' approach is to make your way through the maze, while choosing how to turn at intersections as follows: Always turn left if you can. If you cannot turn left, go straight. If you cannot turn left, or go straight, turn right.",
    "Right Hand Rule": "The 'Right Hand Rule' approach is similar to the 'Left Hand Rule': Instead of always turning left, always turn right. If you cannot turn right, go straight. If you cannot turn right or go straight, turn left.",
    "Breadth First Search": "This algorithm explores all nodes at the present depth prior to moving on to the nodes at the next depth level. It is an uninformed search algorithm.\nGuarantees shortest path.",
    "Depth First Search": "This algorithm starts at the root node and explores as far as possible along each branch before backtracking. It is an uninformed search algorithm.\nDoes not guarantee shortest path",
    "A* Search": "This algorithm is the most optimal in terms of time efficiency. It is an informed search algorithm that utilises 2 heuristics to find the shortest path.\nGuarantees shortest path.",
    "Greedy Best First Search": "This algorithm is an informed search algorithm that only utilises one heuristic function that always chooses the path which appear best at the moment.\nDoes not guarantee shortest path.",
    "Free Roam": "Use Arrow keys to move around. Have fun!"
}

currentAlgo = 0

root = t.Screen()
ogTitle = f"PIZZA RUNNER: {ALGO_LIST[currentAlgo]} | Number of steps: 0 | Timer: 00:00"
root.title(ogTitle)
title = ogTitle
root.setup(1200, 675)
root.cv._rootwindow.resizable(False, False)

character = None
heading = None
maze = None
isRunning = False
algoText = None
startBtn = None
firstTime = True

def updateTimer():
    global character
    global maze
    global isRunning
    if character.state:
        updateTitle()
    isRunning = True
    root.ontimer(updateTimer, 1000)
    return


def updateTitle():
    global title
    titleArr = title.split(" | Timer: ")
    stepArr = titleArr[0].split("steps: ")
    stepArr[1] = str(character.step)
    titleArr[0] = "steps: ".join(stepArr)
    time = datetime.strptime(titleArr[1], "%M:%S")
    time += timedelta(seconds=1)
    titleArr[1] = time.strftime("%M:%S")
    title = " | Timer: ".join(titleArr)
    root.title(title)


def resetTitle():
    global ogTitle
    global title
    ogTitle = f"PIZZA RUNNER: {ALGO_LIST[currentAlgo]} | Number of steps: 0 | Timer: 00:00"
    title = ogTitle
    root.title(ogTitle)


def start():
    global character
    global heading
    global maze
    global isRunning
    global startBtn
    global firstTime
    resetTitle()
    headingText = heading.getText()
    if " Unsolvable" in headingText:
        headingText = headingText.split(" Unsolvable")[0]
    if not character.state and not maze.state:
        resetTitle()
        heading.changeText(headingText + " " + ALGO_LIST[currentAlgo])
        if not isRunning:
            updateTimer()
        solvable = character.start(ALGO_LIST[currentAlgo], firstTime)
        updateTitle()
        if solvable:
            heading.changeText(headingText)
        else:
            heading.changeText(headingText + " Unsolvable")
        startBtn.reset()
    elif not character.state:
        startBtn.reset()
    firstTime = False

# ! to be removed
def turnLeft():
    global character
    character.turnLeft()

def custom_map():
    print("hi")

def breakText(string, maxLength = 30):
    words = string.split()
    lines = []
    line = ""
    for word in words:
        if len(line) + len(word) + 1 <= maxLength:
            line += word + " "
        else:
            lines.append(line)
            line = word + " "
    lines.append(line)
    return "\n".join(lines)


def switchAlgo():
    global character
    global currentAlgo
    global startBtn
    global algoText
    if not character.state:
        currentAlgo += 1
        if currentAlgo > len(ALGO_LIST) - 1:
            currentAlgo = 0
        algoText.changeText(
            f"Algorithm Information:\n{ALGO_LIST[currentAlgo]}\n\n{breakText(ALGO_INFO[ALGO_LIST[currentAlgo]])}")
        resetTitle()
        startBtn.reset()
    else:
        print("Algorithm cannot be switched when turtle is running")

def save_maze():
    global maze
    fileMsg = "Enter save filename/filepath"
    while True:
        filePath = root.textinput(fileMsg, fileMsg)
        if filePath[-4:] != ".txt":
            fileMsg = "Invalid filename/filepath! Enter save filename/filepath"
            continue
        if ":\\" not in filePath:
            filePath = os.path.abspath(
                os.getcwd()) + "\\" + filePath
        break
    maze.saveFile(filePath)
    return 

def generate_maze():
    global maze
    global character
    if not maze.state and not character.state:
        rows, cols = getRowsAndCols()
        maze.generate_maze(rows, cols, root)
        if character is not None:
            character.reset_everything()

def getRowsAndCols():
    rowsMsg = "Enter total number of rows"
    while True:
        try:
            rows = root.textinput(rowsMsg, rowsMsg)
            rows = int(rows)
            if rows > 4 and rows % 2 != 0:
                break
            else:
                rowsMsg = "Row number must be at least 5, must be odd and whole number! Enter total number of rows"
        except ValueError:
            rowsMsg = "Invalid row number! Enter total number of rows"
    colsMsg = "Enter total number of cols"
    while True:
        try:
            cols = root.textinput(colsMsg, colsMsg)
            cols = int(cols)
            if cols > 4 and cols % 2 != 0:
                break
            else:
                colsMsg = "Col number must be at least 5, must be odd and whole number! Enter total number of cols"
        except ValueError:
            colsMsg = "Invalid col number! Enter total number of cols"
    return rows, cols

def main():
    global character
    global heading
    global maze
    global algoText
    global startBtn
    filePath = None
    random = False
    if (len(sys.argv) == 1):
        print("Using default maze")
        filePath = "example.txt"
    if not filePath:
        txtFile = sys.argv[1]
        if txtFile == "random":
            print("Generating random map")
            random = True
        elif txtFile[-4:] != ".txt":
            print("Invalid file type")
            return
        filePath = txtFile
    if not random:
        if ":\\" not in filePath:
            filePath = os.path.abspath(
                os.getcwd()) + "\\" + filePath
        try:
            open(filePath, 'r', encoding="utf8")
        except FileNotFoundError:
            print("File does not exist! Please try again!")
            return
    maze = Maze(root)
    if not random:
        error = maze.upload_map(filePath)
        if error:
            print(f"Map Upload Error: {error}")
            return
    else:
        generate_maze()
    heading = Text("PIZZA RUNNERS:", root, x=0,
                   y=285, bold="bold", fontSize=24)
    heading.draw()
    doneBy = Text("Done by Soh Hong Yu and Samuel Tay Tze Ming from DAAA/FT/2B/01",
                  root, x=0, y=250, bold="bold", fontSize=20)
    doneBy.draw()
    maze.draw_map(root)
    character = Character(
        canvas=root, x=maze.hashmap['start'][0].x, y=maze.hashmap['start'][0].y, maze=maze, size=maze.size)
    instructions = Text("Controls\n" + breakText('1.Press Tab to switch algorithms') + "\n" + breakText("2. Press Space to start algorithm") + "\n" + breakText("3. Press P to pause to switch algorithm") + "\n" + breakText("4. Press R to generate random maze") + "\n" + breakText("5. Press C to create custom maze"),
                        root, x=maze.endX - maze.size * 2, y=-maze.startY + maze.size, bold="normal", fontSize=14, align="right")
    instructions.draw()
    algoText = Text(f"Algorithm Information:\n{ALGO_LIST[currentAlgo]}\n\n{breakText(ALGO_INFO[ALGO_LIST[currentAlgo]])}",
                    root, x=-maze.endX + maze.size * 2, y=-maze.startY + maze.size, bold="normal", fontSize=14, align="left")
    algoText.draw()
    customMapBtn = Button(root, x=-200, y=-250, startShape="square",
                          text="Custom Map", size=3.25, clickFunc=custom_map)
    customMapBtn.draw()
    wallBtn = Button(root, x=-100, y=-250, startShape="square",
                     text="Add Wall", size=3.25, clickFunc=turnLeft, clickText="Remove Wall")
    wallBtn.draw()
    randomMapBtn = Button(root, x=100, y=-250, startShape="square",
                      text="Generate\nRandom Map", size=3.25, clickFunc=generate_maze)
    randomMapBtn.draw()
    saveMapBtn = Button(root, x=200, y=-250, startShape="square",
                      text="Save Map", size=3.25, clickFunc=save_maze)
    saveMapBtn.draw()
    startBtn = Button(root, x=0, y=-250, startShape="turtle", text="START",
                      size=3.25, clickFunc=start, clickText="RUNNING")
    startBtn.draw()
    root.delay(0)
    root.listen()
    root.onkey(switchAlgo, 'Tab')
    root.onkey(start, 'space')
    root.onkey(generate_maze, 'r')
    root.onkey(custom_map, 'c')
    root.onkey(character.updateState, "p")
    root.ontimer(updateTimer, 1)
    root.mainloop()
    return


if __name__ == "__main__":
    main()
