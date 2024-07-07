FONT=("Courier",24,"normal")
from turtle import *
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level=1
        self.goto(-230,250)
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:{self.level}",align="center",font=FONT)
    def increase_level(self):
        self.level+=1
        self.update_scoreboard()
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=FONT )