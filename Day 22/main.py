from turtle import Screen
from paddle import Paddle
import time
import ball
import score
screen=Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800,height=600)


pad=Paddle()
pad.create()
ball=ball.Ball()

screen.listen()
pad.movement()
game=True

score=score.Score()
score.ladd()
score.radd()
while game:
    screen.update()
    time.sleep(0.05)

    game=ball.move(pad.right,pad.left)
    #if game==False:
     #     break
    
    
    
    
    
    
screen.exitonclick()
