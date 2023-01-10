from turtle import RawTurtle


class Character(RawTurtle):
    def __init__(self,canvas=None,x=0,y=0):
        super().__init__(canvas)
        self.hideturtle()
        self.shape('turtle')
        self.pencolor('black')
        self.penup()
        self.setpos(x,y)
        self.showturtle()
        
