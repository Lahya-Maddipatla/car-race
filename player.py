STARTING_POSITION=(0,-280)
from turtle import *
MOVE_DISTANCE=10
FINISH_LINE=250
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        
    def move_forward(self):
        self.forward(MOVE_DISTANCE)
    def go_to_start(self):
        self.goto(STARTING_POSITION)
    def is_at_finish_line(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False
