from turtle import Screen, Turtle

TILE_SIZE = 24
CURSOR_SIZE = 20

class Pen(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(TILE_SIZE / CURSOR_SIZE)
        self.pencolor('black')
        self.penup()
        self.speed('fastest')

def setup_maze(level):
    maze_height, maze_width = len(level), len(level[0])
    for y in range(maze_height):
        for x in range(maze_width):
            character = level[y][x]
            pen.fillcolor(['white', 'grey'][character == 'X'])
            screen_x = (x - maze_width) * TILE_SIZE
            screen_y = (maze_width - y) * TILE_SIZE
            pen.goto(screen_x, screen_y)
            pen.stamp()
            
screen = Screen()
screen.setup(700, 700)
screen.title("PIZZA RUNNERS")

maze = []

with open("example.txt") as file:
    for line in file:
        maze.append(line.strip())

pen = Pen()

setup_maze(maze)

screen.mainloop()
