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

ALGO_LIST = ["Left Hand Rule", "Right Hand Rule", "Breadth First Search", "Depth First Search", "A* Search", "Greedy Best First Search"]
currentAlgo = 0

root = t.Screen()
root.title("Pizza Runners")
root.setup(1200, 675)
root.cv._rootwindow.resizable(False, False)

character = None

def start():
    global character
    if not character.state:
        character.start(ALGO_LIST[currentAlgo])

def turnLeft():
    global character
    character.turnLeft()

def turnRight():
    global character
    character.turnRight()

def main():
    global character
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
    title = Text("Pizza Runners", root, x=0,y=250, bold="bold", fontSize=24)
    title.draw()
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
    root.mainloop()
    return


if __name__ == "__main__":
    main()
