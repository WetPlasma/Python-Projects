import turtle

class Score():
    def __init__(self) -> None:
        self.value=int(0)
        self.point=turtle.Turtle()
        self.point.penup()
        self.point.goto(0,250)
        self.point.color("white")
        self.point.hideturtle()
        self.point.write(f"score = {self.value}",align="center",font=('Arial',15,'bold'))
      
    def inc(self):
        self.value+=1
        self.point.clear()
        self.point.write(f"score = {self.value}",align="center",font=('Arial',15,'bold'))