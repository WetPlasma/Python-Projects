import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self) -> None:
        self.allcars = []
        self.movespeed = STARTING_MOVE_DISTANCE

    def createcars(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            newcar = Turtle()
            newcar.shape("square")
            newcar.penup()
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.color(random.choice(COLORS))
            randy = random.randint(-250, 250)
            newcar.goto(300, randy)
            self.allcars.append(newcar)

    def movecar(self):
        for car in self.allcars:
            car.backward(self.movespeed)

    def speed(self):
        self.movespeed += 10
