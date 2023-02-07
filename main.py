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

# Import Libraries
import sys
import os
import turtle as t
from Maze.Maze import Maze
from Character.Character import Character
from Screen.Text import Text
from Screen.Button import Button
from datetime import datetime, timedelta

# Create Algorithm List ~ Hong Yu + Samuel
ALGO_LIST = ["Left Hand Rule", "Right Hand Rule", "Breadth First Search",
             "Depth First Search", "A* Search", "Greedy Best First Search", "Free Roam"]

# Create Algorithm Information to be displayed ~ Samuel
ALGO_INFO = {
    "Left Hand Rule": "The 'Left Hand Rule' approach is to make your way through the maze, while choosing how to turn at intersections as follows: Always turn left if you can. If you cannot turn left, go straight. If you cannot turn left, or go straight, turn right.",
    "Right Hand Rule": "The 'Right Hand Rule' approach is similar to the 'Left Hand Rule': Instead of always turning left, always turn right. If you cannot turn right, go straight. If you cannot turn right or go straight, turn left.",
    "Breadth First Search": "This algorithm explores all nodes at the present depth prior to moving on to the nodes at the next depth level. It is an uninformed search algorithm.\nGuarantees shortest path.",
    "Depth First Search": "This algorithm starts at the root node and explores as far as possible along each branch before backtracking. It is an uninformed search algorithm.\nDoes not guarantee shortest path",
    "A* Search": "This algorithm is the most optimal in terms of time efficiency. It is an informed search algorithm that utilises 2 heuristics to find the shortest path.\nGuarantees shortest path.",
    "Greedy Best First Search": "This algorithm is an informed search algorithm that only utilises one heuristic function that always chooses the path which appear best at the moment.\nDoes not guarantee shortest path.",
    "Free Roam": "Use Arrow keys to move around. Have fun!"
}

# Zero based index to select algorithm
currentAlgo = 0

# Setup root screen ~ Hong Yu
root = t.Screen()
ogTitle = f"PIZZA RUNNER: {ALGO_LIST[currentAlgo]} | Number of steps: 0 | Timer: 00:00"
root.title(ogTitle)
title = ogTitle
root.setup(1200, 675)
root.cv._rootwindow.resizable(False, False)

# Setup global variables as None ~ Hong Yu + Samuel
character = None
heading = None
maze = None
isRunning = False
algoText = None
startBtn = None
firstTime = True
customMapBtn = None
wallBtn = None
addStartBtn = None
addEndBtn = None

# UI Improvements ~ Hong Yu
# Update timer
def updateTimer():
    global character
    global maze
    global isRunning
    # Check the state of the character
    if character.state:
        updateTitle()
    isRunning = True
    root.ontimer(updateTimer, 1000)
    return

# Update title ~ Hong Yu
def updateTitle():
    global title
    # Split to get and edit the different parts of the title
    titleArr = title.split(" | Timer: ")
    stepArr = titleArr[0].split("steps: ")
    stepArr[1] = str(character.step)
    titleArr[0] = "steps: ".join(stepArr)
    time = datetime.strptime(titleArr[1], "%M:%S")
    time += timedelta(seconds=1)
    titleArr[1] = time.strftime("%M:%S")
    title = " | Timer: ".join(titleArr)
    root.title(title)

# Reset title ~ Hong Yu
def resetTitle():
    global ogTitle
    global title
    ogTitle = f"PIZZA RUNNER: {ALGO_LIST[currentAlgo]} | Number of steps: 0 | Timer: 00:00"
    title = ogTitle
    root.title(ogTitle)
    
# Break Text if string is too long ~ Hong Yu
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

# Main Functionalities
# Start algorithms ~ Hong Yu + Samuel
def start():
    # Access global variables
    global character
    global heading
    global maze
    global isRunning
    global startBtn
    global firstTime
    global customMapBtn
    # Check if custom is running
    if customMapBtn.toggleState:
        return
    # Reset title
    resetTitle()
    # Modify the heading
    headingText = heading.getText()
    if " Unsolvable" in headingText:
        headingText = headingText.split(" Unsolvable")[0]
    # Ensure character and maze is not on edit mode
    if not character.state and not maze.state:
        # Reset title for timer and step counter
        resetTitle()
        heading.changeText(headingText + " " + ALGO_LIST[currentAlgo])
        if not isRunning:
            updateTimer()
        solvable = character.start(ALGO_LIST[currentAlgo], firstTime)
        updateTitle()
        # Checks if solvable
        if solvable:
            heading.changeText(headingText)
        else:
            heading.changeText(headingText + " Unsolvable")
        # Reset startBtn
        startBtn.reset()
    elif not character.state:
        # Reset startBtn
        startBtn.reset()
    # Remove firstTime run
    firstTime = False

# Switch Algorithms ~ Hong Yu + Samuel
def switchAlgo():
    global character
    global currentAlgo
    global startBtn
    global algoText
    global customMapBtn
    if not customMapBtn.toggleState:
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

# Soh Hong Yu's Additional Features - Custom Maze
# Check x,y position of mouse click
def clickWalls(x, y):
    global maze
    global character
    global customMapBtn
    global wallBtn
    global addStartBtn
    global addEndBtn
    # Hide turtle
    if character is not None:
        character.hideturtle()
    if customMapBtn is not None:
        if customMapBtn.toggleState:
            gotRow = False
            gotCol = False            
            # Loop through to check if the rows/cols are in range of mouse click
            for row in range(maze.rows):
                if y < maze.get_mapArr()[row][0].y + maze.size / 2 and y > maze.get_mapArr()[row][0].y - maze.size / 2:
                    gotRow = True
                    break
            for col in range(maze.columns):
                if x < maze.get_mapArr()[0][col].x + maze.size / 2 and x > maze.get_mapArr()[0][col].x - maze.size / 2:
                    gotCol = True
                    break
            # Loop through and update the map according to the changes
            if gotCol and gotRow:
                if not wallBtn.toggleState:
                    # Check what kind of wall to add
                    if addStartBtn.toggleState:
                        # Ensure that only 1 start and end exist at 1 time
                        for r in range(maze.rows):
                            for c in range(maze.columns):
                                if maze.get_mapArr()[r][c].is_start():
                                    maze.get_mapArr()[r][c].reset()
                                    maze.get_mapArr()[r][c].draw()
                        maze.get_mapArr()[row][col].make_start()  
                        addStartBtn.toggleState = False
                        addStartBtn.updateState()
                    elif addEndBtn.toggleState:
                        for r in range(maze.rows):
                            for c in range(maze.columns):
                                if maze.get_mapArr()[r][c].is_end():
                                    maze.get_mapArr()[r][c].reset()
                                    maze.get_mapArr()[r][c].draw()
                        maze.get_mapArr()[row][col].make_end()    
                        addEndBtn.toggleState = False
                        addEndBtn.updateState()
                    else:
                        maze.get_mapArr()[row][col].make_wall()
                else:
                    maze.get_mapArr()[row][col].reset()
                maze.get_mapArr()[row][col].draw()
                # Generate maze as string
                maze.generate_mapString()


# Add Wall
def addWall():
    global addStartBtn
    global addEndBtn
    global wallBtn
    if addStartBtn.toggleState:
        addStartBtn.toggleState = False
        addStartBtn.updateState()
    if addEndBtn.toggleState:
        addEndBtn.toggleState = False
        addEndBtn.updateState()

# Add End


def addEnd():
    global addStartBtn
    global addEndBtn
    global wallBtn
    if addStartBtn.toggleState:
        addStartBtn.toggleState = False
        addStartBtn.updateState()
    if wallBtn.toggleState:
        wallBtn.toggleState = False
        wallBtn.updateState()

# Add Start
def addStart():
    global addStartBtn
    global addEndBtn
    global wallBtn
    if addEndBtn.toggleState:
        addEndBtn.toggleState = False
        addEndBtn.updateState()
    if wallBtn.toggleState:
        wallBtn.toggleState = False
        wallBtn.updateState()

# Make maze
def make_maze():
    # Global maze
    global maze
    global character
    global customMapBtn
    checkStart = False
    checkEnd = False
    # Check if end and start exist to make sure maze is valid
    for r in range(maze.rows):
        for c in range(maze.columns):
            if maze.get_mapArr()[r][c].is_end():
                checkEnd = True
            if maze.get_mapArr()[r][c].is_start():
                checkStart = True
    if checkStart and checkEnd:
        # Draw map
        maze.draw_map(root)
        maze.generate_mapString()
        character = Character(
            canvas=root, x=maze.hashmap['start'][0].x, y=maze.hashmap['start'][0].y, maze=maze, size=maze.size)
        character.reset_everything()
    else:
        # Reset custom map if cannot find start and end points
        print("No start point/end point found")
        customMapBtn.toggleState = True
        customMapBtn.updateState()
        custom_map()
    root.onscreenclick(None)
    root.mainloop()

# Link to custom map button                
def custom_map():
    global maze
    global character
    global customMapBtn
    # Hide character
    character.hideturtle()
    # Create custom map
    if not maze.state and not character.state:
        rows, cols = getRowsAndCols(True)
        maze.custom_map(rows, cols, root)
        if character is not None:
            character.reset_everything()
            character.hideturtle()
        # Allow click
        root.onscreenclick(clickWalls)
        root.mainloop()
    else:
        customMapBtn.toggleState = False
        customMapBtn.updateState()

# Save maze
def save_maze():
    global maze
    # Get file path and check if file path exist
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
    maze.saveFile(filePath) # Save file based on filepath
    return 

# Soh Hong Yu's Additional Features - Randomized Maze
def generate_maze():
    global maze
    global character
    try:
        if not maze.state and not character.state:
            rows, cols = getRowsAndCols()
            maze.generate_maze(rows, cols, root)
            if character is not None:
                character.reset_everything()
    except AttributeError:
        rows, cols = getRowsAndCols()
        maze.generate_maze(rows, cols, root)

# get row and col for the maze
def getRowsAndCols(allowEven = False):
    rowsMsg = "Enter total number of rows"
    while True:
        try:
            rows = root.textinput(rowsMsg, rowsMsg)
            rows = int(rows)
            if rows >= 5 and rows <= 60:
                if allowEven or rows % 2 != 0:
                    break
                else:
                    rowsMsg = "Row number must be odd! Enter total number of rows"    
            else:
                rowsMsg = "Row number must be between 5 to 60! Enter total number of rows"
        except ValueError:
            rowsMsg = "Invalid row number! Enter total number of rows"
    colsMsg = "Enter total number of cols"
    while True:
        try:
            cols = root.textinput(colsMsg, colsMsg)
            cols = int(cols)
            if cols >= 5 and cols <= 60:
                if allowEven or cols % 2 != 0:
                    break
                else:
                    colsMsg = "Col number must be odd! Enter total number of cols"    
            else:
                colsMsg = "Col number must be between 5 to 60! Enter total number of cols"
        except ValueError:
            colsMsg = "Invalid col number! Enter total number of cols"
    return rows, cols

# Main Function ~ Hong Yu + Samuel
def main():
    # Global Variables
    global character
    global heading
    global maze
    global algoText
    global startBtn
    global customMapBtn
    global wallBtn
    global addStartBtn
    global addEndBtn
    filePath = None
    random = False
    # Get parameters from cmd
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
    # Check if not random and see if file exist
    if not random:
        if ":\\" not in filePath:
            filePath = os.path.abspath(
                os.getcwd()) + "\\" + filePath
        try:
            open(filePath, 'r', encoding="utf8")
        except FileNotFoundError:
            print("File does not exist! Please try again!")
            return
    # Create a maze instance
    maze = Maze(root)
    if not random:
        # Upload map
        error = maze.upload_map(filePath)
        if error:
            print(f"Map Upload Error: {error}")
            return
    elif random:
        # Generate maze
        generate_maze()
    # UI
    heading = Text("PIZZA RUNNERS:", root, x=0,
                   y=285, bold="bold", fontSize=24)
    heading.draw()
    doneBy = Text("Done by Soh Hong Yu and Samuel Tay Tze Ming from DAAA/FT/2B/01",
                  root, x=0, y=250, bold="bold", fontSize=20)
    doneBy.draw()
    maze.draw_map(root)
    character = Character(
        canvas=root, x=maze.hashmap['start'][0].x, y=maze.hashmap['start'][0].y, maze=maze, size=maze.size)
    instructions = Text("Controls\n" + breakText('1.Press Tab to switch algorithms') + "\n" 
                        + breakText("2. Press Space Key to start algorithm") + "\n" 
                        + breakText("3. Press P Key to pause to switch algorithm") + "\n" 
                        + breakText("4. Press R Key to generate random maze") + "\n" 
                        + breakText("5. Press C Key to create custom maze") + "\n"
                        + breakText("6. Use the different toggle buttons to access different options"),
                        root, x=maze.endX - maze.size * 2, y=-maze.startY + maze.size, bold="normal", fontSize=14, align="right")
    instructions.draw()
    algoText = Text(f"Algorithm Information:\n{ALGO_LIST[currentAlgo]}\n\n{breakText(ALGO_INFO[ALGO_LIST[currentAlgo]])}",
                    root, x=-maze.endX + maze.size * 2, y=-maze.startY + maze.size, bold="normal", fontSize=14, align="left")
    algoText.draw()
    addStartBtn = Button(root, x=-300, y=-250, startShape="square",
                     text="Click to\nadd Start", size=3.25, clickText="Adding Start", clickFunc=addStart, toggle=True)
    addStartBtn.draw()
    addEndBtn = Button(root, x=-200, y=-250, startShape="square",
                     text="Click to\nadd End", size=3.25, clickText="Adding End",clickFunc=addEnd, toggle=True)
    addEndBtn.draw()
    wallBtn = Button(root, x=-100, y=-250, startShape="square",
                     text="Add Wall", size=3.25, clickText="Remove Wall", toggle=True, clickFunc=addWall)
    wallBtn.draw()
    customMapBtn = Button(root, x=100, y=-250, startShape="square",
                          text="Custom Map", size=3.25, clickFunc=custom_map, clickText="Running\nCustom Map", toggle=True, toggleFunc=make_maze)
    customMapBtn.draw()
    randomMapBtn = Button(root, x=200, y=-250, startShape="square",
                      text="Generate\nRandom Map", size=3.25, clickFunc=generate_maze)
    randomMapBtn.draw()
    saveMapBtn = Button(root, x=300, y=-250, startShape="square",
                      text="Save Map", size=3.25, clickFunc=save_maze)
    saveMapBtn.draw()
    startBtn = Button(root, x=0, y=-250, startShape="turtle", text="START",
                      size=3.25, clickFunc=start, clickText="RUNNING")
    startBtn.draw()
    root.delay(0)
    root.listen()
    # Key presses
    root.onkey(switchAlgo, 'Tab')
    root.onkey(start, 'space')
    root.onkey(generate_maze, 'r')
    root.onkey(custom_map, 'c')    
    root.onkey(character.updateState, "p")
    root.ontimer(updateTimer, 1)
    root.onscreenclick(None)
    root.mainloop()
    return

# Check and ensure it is the main python file run
if __name__ == "__main__":
    main()
