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

import os
import turtle as t
from Maze.Maze import Maze
from Character.Character import Character
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfile

# Start Tkinter
root = Tk()
root.title(
    'PIZZA RUNNERS: Done by Soh Hong Yu & Samuel Tay Tze Ming, DAAA/FT/2B/01')  # Change
root.geometry('1200x675')
root.config(bg='white')
character = None
# Make toggle btn


# ! You must display the algorithm name, and the number of steps the application took/has taken, in the window’s title bar.

def toggle():
    global toggleBtn
    if toggleBtn.config('relief')[-1] == 'sunken':
        toggleBtn.config(relief="raised", text="Add Walls")
    else:
        toggleBtn.config(relief="sunken", text="Remove Walls")


def start():
    global startBtn
    global character
    if startBtn.config('relief')[-1] == 'sunken':
        startBtn.config(relief="raised", text="Start")
    else:
        startBtn.config(relief="sunken", text="Stop")
        character.start(algoOption.get())


toggleBtn = Button(text="Add Walls", width=12,
                   relief="raised", command=toggle)

startBtn = Button(text="Start", width=12,
                  relief="raised", command=start)

ALGO_LIST = ["Left Hand Rule", "Right Hand Rule", "Breadth First Search",
                "Depth First Search", "A* Search", "Greedy Best First Search"]
algoOption = ttk.Combobox(root, values=ALGO_LIST)

def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Text Files', '*txt')])
    print(file_path.name)
    if file_path is not None:
        pass


def main():
    global character
    # Title
    title = Label(root, text='Pizza Runners')
    title.config(fg='black', bg="white", font="impact 24 bold")
    title.grid(row=0, column=0, columnspan=3, pady=10, padx=50)
    # Menu
    # Algorithm
    algoTitle = Label(root, text='Algorithm')
    algoTitle.config(fg='black', bg="white", font="arial 14")
    algoTitle.grid(row=1, column=1, pady=10, padx=50)
    algoOption.config(width=20)
    algoOption.set(ALGO_LIST[0])
    algoOption['state'] = 'readonly'
    algoOption.grid(row=2, column=1)
    # Map
    mapTitle = Label(root, text='Map')
    mapTitle.config(fg='black', bg="white", font="arial 14")
    mapTitle.grid(row=3, column=1, pady=10, padx=50)
    map_LIST = ["Pre Build 1", "Pre Build 2",
                "Pre Build 3", "Custom", "Random", "Upload"]
    mapOption = ttk.Combobox(root, values=map_LIST)
    mapOption.config(width=20)
    mapOption.set(map_LIST[0])
    mapOption['state'] = 'readonly'
    mapOption.grid(row=4, column=1)
    # Upload
    uploadBtn = Button(
        root,
        text='Upload Map',
        command=lambda: open_file()
    )
    uploadBtn.grid(row=5,  column=1, padx=10)
    # ok_btn = ttk.Button(root, text='Save', style='TButton')
    # ok_btn.grid(row=2, column=3)
    toggleBtn.grid(row=6, column=1)
    startBtn.grid(row=7, column=1)
    canvas = Canvas(root, width=800, height=450)
    canvas.grid(row=1, rowspan=7, column=0, padx=50, sticky=W)
    # Map
    maze = Maze()
    # maze.upload_map()
    maze.draw(canvas)
    # Character
    character = Character(canvas=canvas, x=maze.hashmap['start'][0][0], y=maze.hashmap['start'][0][1], maze=maze)
    root.resizable(False, False)
    root.mainloop()


if __name__ == "__main__":
    main()
