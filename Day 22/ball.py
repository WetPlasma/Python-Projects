from turtle import Turtle , Screen
import paddle,score

ball=Turtle()
screen=Screen()
scoreobj=score.Score()
class Ball:
    def __init__(self) -> None: 
        ball.shape("circle")
        ball.color("white")
        ball.penup()
        screen.listen()
        self.movex=int(20)
        self.movey=int(20)
    def hit(self):
        if ball.xcor()>780 or ball.xcor()<-780:
            ball.clear()
            
    def bounce(self,x):
        self.movex=-self.movex
        pass
    
    def move(self,right,left):
        self.newx = ball.xcor() + self.movex
        self.newy = ball.ycor() + self.movey
        ball.goto(self.newx,self.newy)
        if ball.ycor()>260 or ball.ycor()<-260:
            self.movey=-self.movey
        if ball.distance(right)<50 and ball.xcor()>320:
            self.bounce(ball.xcor())
            scoreobj.radd()
        if ball.distance(left)<50 and ball.xcor()<-320:
            self.bounce(ball.xcor())
            scoreobj.ladd()
        elif ball.xcor()>380 or ball.xcor()<-380:
            print("bal out of bounds. resetting")
            ball.goto(x=0,y=0)
            #return False
        return True