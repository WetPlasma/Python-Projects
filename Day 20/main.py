from turtle import Screen,Turtle
import time,food,score
from snake import Snake

# Screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Create snake
snake = Snake()
food = food.Food()
score=score.Score()
# Set up key listeners
screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    #collision
    if snake.head.distance(food)<15:
        print("lol")
        food.refresh()
        score.inc()
        snake.add_segment()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        over=Turtle()
        over.color("white")
        over.hideturtle()
        over.write(f"GAME OVER",align="center",font=('Arial',15,'bold'))
        game_is_on=False
    for segs in snake.segments:
        if segs == snake.segments[0] or segs == snake.segments[1] or segs == snake.segments[2]:
            continue
        if snake.head.distance(segs)<10:
            over=Turtle()
            over.color("white")
            over.hideturtle()
            over.write(f"GAME OVER",align="center",font=('Arial',15,'bold'))
            game_is_on=False
        

screen.exitonclick()