from turtle import Turtle,Screen
screen = Screen()
class Paddle:
    def __init__(self) -> None:
        pass
    
    def create(self):
        self.left=Turtle()
        self.left.penup()
        self.left.shape("square")
        self.left.color("white")
        self.left.shapesize(stretch_wid=5,stretch_len=1)
        self.left.goto(x=-350,y=0)
        print(self.left.turtlesize())  # Outputs (stretch_wid, stretch_len, outline)

                   
        self.right=Turtle()
        self.right.penup()
        self.right.shape("square")
        self.right.color("white")
        self.right.shapesize(stretch_wid=5,stretch_len=1)
        self.right.goto(x=350,y=0)
        
        
    def upl(self):
        if self.left.ycor() < 250:  # Check upper boundary
            self.left.sety(self.left.ycor() + 20)

    def downl(self):
        if self.left.ycor() > -250:  # Check lower boundary
            self.left.sety(self.left.ycor() - 20)

    def upr(self):
        if self.right.ycor() < 250:  # Check upper boundary
            self.right.sety(self.right.ycor() + 20)

    def downr(self):
        if self.right.ycor() > -250:  # Check lower boundary
            self.right.sety(self.right.ycor() - 20)
    # Move the right paddle down
    
    def dummy(self):
        pass
    # Bind keys to paddle movement
    def movement(self):
        screen.onkeypress(self.upl, "w")
        screen.onkeyrelease(self.dummy, "w")
        screen.onkeypress(self.downl, "s")
        screen.onkeyrelease(self.dummy, "s")   
        screen.onkeypress(self.upr, "Up")
        screen.onkeyrelease(self.dummy, "Up")    
        screen.onkeypress(self.downr, "Down")
        screen.onkeyrelease(self.dummy, "Down")
    
    def padlret(self):
        return (self.left.xcor(),self.left.ycor())