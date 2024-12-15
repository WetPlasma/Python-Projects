from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    race_on = True
else:
    race_on = False

while race_on:
    for turtle in all_turtles:
        turtle.forward(randint(0, 10))
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations! The {winning_color} turtle won, and your bet was correct!")
            else:
                print(f"Sorry! The {winning_color} turtle won. Better luck next time!")

screen.exitonclick()
