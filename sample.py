"""
A maze-solving exercise using the "turtle" module.

The student should implement a new function and make it be executed in the indicated place at the bottom of the module.
The function should use "turtle.peek()", "turtle.forward()", "turtle.left()", and "turtle.right()", but the arguments to
"left" and "right" should be divisible by 90.

Monkey-patches "peek" and "forward" in "turtle" to address the fact that a turtle can't get the color of the pixel beneath it
and to restrict movement to the grid.
"""
#I wouldn't call this code "good", but it works and is relatively small.

import turtle
import random
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
minx_px = -300; miny_px = 300; grid_px = 20
max_pt = Point(25, 25)

def generate_maze():
  """
  Draws a random maze and returns the datastructure that represents it
  
  The path of the maze is drawn as lines, not as corridors.
  The returned datastructure is a list of maze rows, where each row is a dict of "up", "down", "left", "right"
  mapping to a bool, indicating whether that direction is possible for travel.
  """
  maze = [[dict.fromkeys(['up', 'down', 'left', 'right'], False) 
    for x in range(max_pt.x)] for y in range(max_pt.y)]
  
  cur_pt = Point(0, max_pt.y/2)
  stack = []
  first = True

  turtle.penup()
  turtle.pencolor('orange')
  turtle.goto(*scale_maze_to_grid(cur_pt))
  turtle.pensize(10)
  turtle.speed(10)
  turtle.pendown()

  while stack or first:
    first = False

    directions = {'up': (0,-1), 'down': (0,1), 'left': (-1,0), 'right': (1,0)}
    neighbors = {
      direction: Point(x, y)
      for x,y,direction in [(cur_pt.x + v[0], cur_pt.y + v[1], k) for k,v in directions.items()]
      if 0 <= x < max_pt.x and 0 <= y < max_pt.y      #check bounds
      if all(v==False for v in maze[y][x].values())   #Not explored yet
    }

    if neighbors:
      stack.append(cur_pt)
      direction = random.choice(neighbors.keys())
      
      new_cur_pt = neighbors[direction]
      maze[cur_pt.y][cur_pt.x][direction] = True
      
      opp = {'up': 'down', 'left': 'right', 'down': 'up', 'right': 'left'}
      maze[new_cur_pt.y][new_cur_pt.x][opp[direction]] = True
      
      cur_pt = new_cur_pt
      turtle.goto(*scale_maze_to_grid(cur_pt))
    else:
      cur_pt = stack.pop()
      turtle.goto(*scale_maze_to_grid(cur_pt))

  turtle.penup()
  return maze

# Helper functions
def scale_maze_to_grid(pt):
  return pt.x*grid_px + minx_px, -(pt.y*grid_px) + miny_px


def scale_grid_to_maze(pt):
  return int(pt.x - minx_px)/grid_px, int(-pt.y + miny_px)/grid_px


def peek(maze):
  '''Returns True if the turtle can move forwards, else False'''
  pt = scale_grid_to_maze(Point(*turtle.pos()))
  heading = turtle.heading()
  if not heading % 90 == 0:
    raise ValueError("Turtle is not facing in a cardinal direction!")

  directions = {0: 'right', 90: 'up', 180: 'left', 270: 'down'}
  return maze[pt[1]][pt[0]][directions[heading]]

turtle.peek = peek


turtle._old_forward = turtle.forward

def forward():
  '''Moves the turtle forward 1 step'''
  turtle._old_forward(grid_px)

turtle.forward = forward


maze = generate_maze()
#Student function goes here
turtle.mainloop()
