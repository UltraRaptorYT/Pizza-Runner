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
    "Free Roam": "Have fun"
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
    print("Hello World")
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
    resetTitle()
    if not character.state and not maze.state:
        resetTitle()
        headingText = heading.getText()
        heading.changeText(headingText + " " + ALGO_LIST[currentAlgo])
        if not isRunning:
            updateTimer()
        character.start(ALGO_LIST[currentAlgo])
        updateTitle()
        heading.changeText(headingText)


def turnLeft():
    global character
    character.turnLeft()


def turnRight():
    global character
    character.turnRight()


def breakText(string, maxLength = 25):
    outputArr = []
    stringArr = string.split()
    counter = 0
    lineArr = []
    while counter < len(stringArr):
        lineArr.append(stringArr[counter])
        if len(" ".join(lineArr)) > maxLength:
            outputArr.append(" ".join(lineArr))
            lineArr = []
        counter += 1
    return "\n".join(outputArr)


def switchAlgo():
    global character
    global currentAlgo
    global algoText
    if not character.state:
        currentAlgo += 1
        if currentAlgo > len(ALGO_LIST) - 1:
            currentAlgo = 0
        algoText.changeText(
            f"Algorithm Information:\n{ALGO_LIST[currentAlgo]}\n\n{breakText(ALGO_INFO[ALGO_LIST[currentAlgo]])}")
        resetTitle()
    else:
        print("Algorithm cannot be switched when turtle is running")


def main():
    global character
    global heading
    global maze
    global algoText
    filePath = None
    if (len(sys.argv) == 1):
        print("Using default maze")
        filePath = "example.txt"
    if not filePath:
        txtFile = sys.argv[1]
        if txtFile[-4:] != ".txt":
            print("Invalid file type")
            return
        filePath = txtFile
    if ":\\" not in filePath:
        filePath = os.path.abspath(
            os.getcwd()) + "\\" + filePath
    try:
        open(filePath, 'r', encoding="utf8")
    except FileNotFoundError:
        print("File does not exist! Please try again!")
        return
    maze = Maze()
    error = maze.upload_map(filePath)
    if error:
        print(f"Map Upload Error: {error}")
        return
    heading = Text("PIZZA RUNNERS:", root, x=0,
                   y=285, bold="bold", fontSize=24)
    heading.draw()
    doneBy = Text("Done by Soh Hong Yu and Samuel Tay Tze Ming from DAAA/FT/2B/01",
                  root, x=0, y=250, bold="bold", fontSize=20)
    doneBy.draw()
    maze.draw_map(root)
    # root.textinput("hi",'hi')
    character = Character(
        canvas=root, x=maze.hashmap['start'][0][0], y=maze.hashmap['start'][0][1], maze=maze, size=maze.size)
    instructions = Text("Controls\n1.\n2.\n3.",
                        root, x=maze.endX - maze.size * 4, y=0, bold="normal", fontSize=14, align="right")
    instructions.draw()
    algoText = Text(f"Algorithm Information:\n{ALGO_LIST[currentAlgo]}\n\n{breakText(ALGO_INFO[ALGO_LIST[currentAlgo]])}",
                    root, x=-maze.endX + maze.size * 2, y=-maze.startY + maze.size, bold="normal", fontSize=14, align="left")
    algoText.draw()
    wallBtn = Button(root, x=-100, y=-250, startShape="square",
                     text="Turn Left", size=3, clickFunc=turnLeft)
    wallBtn.draw()
    otherBtn = Button(root, x=100, y=-250, startShape="square",
                      text="Turn Right", size=3, clickFunc=turnRight)
    otherBtn.draw()
    startBtn = Button(root, x=0, y=-250, startShape="turtle", text="START",
                      size=3, clickFunc=start, clickText="RUNNING")
    startBtn.draw()
    print(filePath)
    root.delay(0)
    root.listen()
    root.onkey(switchAlgo, 'Tab')
    root.onkey(start, 'space')
    root.ontimer(updateTimer, 1)
    root.mainloop()
    return


if __name__ == "__main__":
    main()
