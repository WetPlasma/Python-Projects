import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()

screen.listen()
screen.onkey(player.go_up, "Up")
carmanager = CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.createcars()
    carmanager.movecar()

    # collision

    for car in carmanager.allcars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            game_is_on = False
    # level comp

    if player.ycor() > 280:
        player.goto(0, -280)
        carmanager.speed()
        scoreboard.inclevel()
screen.exitonclick()
