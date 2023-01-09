"""
Member 1:
Name: Soh Hong Yu
Class: DAAA/FT/2B/01
Admin No.: P2100775
Member 2:
Name: Samuel Tay Tze Ming
Class: DAAA/FT/2B/01
Admin No.: P210
"""

import os
import turtle as t
from Maze import Maze
from tkinter import *
from tkinter import ttk, messagebox
from tkinter.filedialog import askopenfile

# Start Tkinter
root = Tk()
root.title(
    'PIZZA RUNNERS: Done by Soh Hong Yu & Samuel Tay Tze Ming, DAAA/FT/2B/01')  # Change
root.geometry('1200x675')
root.config(bg='white')

# Make toggle btn
def toggle():
    global toggle_btn
    if toggle_btn.config('relief')[-1] == 'sunken':
        toggle_btn.config(relief="raised", text="Add Walls")
    else:
        toggle_btn.config(relief="sunken", text="Remove Walls")

toggle_btn = Button(text="Add Walls", width=12, relief="raised", command=toggle)


def open_file():
    file_path = askopenfile(mode='r', filetypes=[('Image Files', '*jpeg')])
    if file_path is not None:
        pass

def main():
    # Title
    title = Label(root, text='Pizza Runners')
    title.config(fg='black', bg="white", font="impact 24 bold")
    title.grid(row=0, column=0, pady=10, padx=50, sticky=N)
    # Menu
    # Algorithm
    algoTitle = Label(root, text='Algorithm')
    algoTitle.config(fg='black', bg="white", font="arial 14")
    algoTitle.grid(row=1, column=1, pady=10, padx=50)
    ALGO_LIST = ["Left Hand Rule", "Right Hand Rule", "Breadth First Search", "Depth First Search", "A* Search", "Greedy Best First Search"]
    algoOption = ttk.Combobox(root, values=ALGO_LIST)
    algoOption.config(width=20)
    algoOption.set(ALGO_LIST[0])
    algoOption['state'] = 'readonly'
    algoOption.grid(row=2, column=1)
    # Map
    mapTitle = Label(root, text='Map')
    mapTitle.config(fg='black', bg="white", font="arial 14")
    mapTitle.grid(row=3, column=1, pady=10, padx=50)
    map_LIST = ["Pre Build 1", "Pre Build 2","Pre Build 3", "Custom", "Random", "Upload"]
    mapOption = ttk.Combobox(root, values=map_LIST)
    mapOption.config(width=20)
    mapOption.set(map_LIST[0])
    mapOption['state'] = 'readonly'
    mapOption.grid(row=4, column=1)
    # Upload
    # colors = ["Pre Build 1", "Pre Build 2",
    #           "Pre Build 3", "Custom", "Random", "Upload"]
    # selectOption = ttk.Combobox(root, values=colors)
    # selectOption.config(width=20)
    # selectOption.set(colors[0])
    # selectOption['state'] = 'readonly'
    # selectOption.grid(row=1, column=2, sticky=E)
    # ok_btn = ttk.Button(root, text='Save', style='TButton')
    # toggle_btn.grid(row=1, column=3)
    # ok_btn.grid(row=2, column=3)
    canvas = Canvas(root, width=800, height=450)
    canvas.grid(row=1, rowspan=7,column=0, padx=50, sticky=W)
    tk = t.RawTurtle(canvas)
    maze = Maze(tk)
    # maze.draw(tk)
    root.resizable(False, False)
    root.mainloop()

if __name__ == "__main__":
    main()
