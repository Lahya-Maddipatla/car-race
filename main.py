from turtle import *
from car_manager import Carmanager
from player import Player
from scoreboard import Scoreboard
import time

screen=Screen()
screen.tracer(0)
player=Player()
carmanager=Carmanager()
scoreboard=Scoreboard()
screen.setup(600,600)
screen.listen()
screen.onkey(player.move_forward,"Up")
game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_cars()
    carmanager.move_cars()
    for car in carmanager.all_cars:
        if car.distance(player)<20:
            game_is_on=False
            scoreboard.game_over()
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.level_up()
        scoreboard.increase_level()

screen.exitonclick()