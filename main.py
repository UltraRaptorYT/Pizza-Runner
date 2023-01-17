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

ALGO_LIST = ["Left Hand Rule", "Right Hand Rule", "Breadth First Search", "Depth First Search", "A* Search", "Greedy Best First Search"]
currentAlgo = 0

root = t.Screen()
ogTitle = f"PIZZA RUNNER: {ALGO_LIST[currentAlgo]} | Number of steps: 0 | Timer: 00:00"
root.title(ogTitle)
title = ogTitle
root.setup(1200, 675)
root.cv._rootwindow.resizable(False, False)

character = None
heading = None

def updateTimer():
    global character
    if character.state:
        updateTitle()
    root.ontimer(updateTimer, 1000)
    return

def updateTitle():
    global title
    titleArr = title.split(" | Timer: ")
    stepArr = titleArr[0].split("steps: ")
    stepArr[1] = str(character.step)
    titleArr[0] = "steps: ".join(stepArr)
    time = datetime.strptime(titleArr[1],"%M:%S")
    time += timedelta(seconds=1)
    titleArr[1] = time.strftime("%M:%S")
    title = " | Timer: ".join(titleArr)
    root.title(title)

def resetTitle():
    global ogTitle
    global title
    ogTitle = f"PIZZA RUNNER: {ALGO_LIST[currentAlgo]} | Number of steps: 0 | Timer: 00:00"
    root.title(ogTitle)
    title = ogTitle

def start():  
    resetTitle()  
    global character
    global heading
    if not character.state:
        headingText = heading.getText()
        heading.changeText(headingText + " " + ALGO_LIST[currentAlgo])
        character.start(ALGO_LIST[currentAlgo])
        updateTitle()
        heading.changeText(headingText)


def turnLeft():
    global character
    character.turnLeft()

def turnRight():
    global character
    character.turnRight()


def switchAlgo():
    global character
    global currentAlgo
    if not character.state:
        currentAlgo += 1
        if currentAlgo > len(ALGO_LIST) - 1:
            currentAlgo = 0
        resetTitle()
    else:
        print("Algorithm cannot be switched when turtle is running")

def main():
    global character
    global heading
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
        print("Map Error")
        return
    heading = Text("PIZZA RUNNERS:", root, x=0,y=250, bold="bold", fontSize=24)
    heading.draw()
    doneBy = Text(" Done by Soh Hong Yu and Samuel Tay Tze Ming from DAAA/FT/2B/01",
                  root, x=0, y=200, bold="bold", fontSize=20)
    doneBy.draw()
    maze.draw_map(root)
    # root.textinput("hi",'hi')
    character = Character(canvas=root, x=maze.hashmap['start'][0][0], y=maze.hashmap['start'][0][1], maze=maze)
    wallBtn = Button(root, x=-100, y=-250, startShape="square",text="Turn Left", size=3, clickFunc=turnLeft)
    wallBtn.draw()
    otherBtn = Button(root, x=100, y=-250, startShape="square",text="Turn Right", size=3, clickFunc=turnRight)
    otherBtn.draw()
    startBtn = Button(root, x=0, y=-250, startShape="turtle", text="START",
                      size=3, clickFunc=start, clickText="RUNNING")
    startBtn.draw()
    print(filePath)
    root.listen()
    root.onkey(switchAlgo, 'Tab')
    root.ontimer(updateTimer, 1000)
    root.mainloop()
    return


if __name__ == "__main__":
    main()
