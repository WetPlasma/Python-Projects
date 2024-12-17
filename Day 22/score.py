from turtle import Turtle, Screen

class Score:
    def __init__(self) -> None:
        self.Rscore = 0  # Initialize scores to 0
        self.Lscore = 0
        self.screen = Screen()
        self.screen.listen()

        # Create turtles for score display
        self.rscore = self.create_score_turtle(100, 250)
        self.lscore = self.create_score_turtle(-100, 250)

        # Display initial scores
        self.update_score(self.rscore, self.Rscore)
        self.update_score(self.lscore, self.Lscore)

    def create_score_turtle(self, x, y):
        score_turtle = Turtle()
        score_turtle.color("white")
        score_turtle.hideturtle()
        score_turtle.penup()
        score_turtle.goto(x, y)
        score_turtle.pendown()
        return score_turtle

    def update_score(self, score_turtle, score):
        score_turtle.clear()  # Clear the previous score
        score_turtle.write(f"{score}", align="center", font=('Arial', 20, 'bold'))

    def ladd(self):
        self.Lscore += 1
        self.lscore.clear()  # Clear the previous score
        self.lscore.penup()
        self.lscore.goto(-100, 250)  # Set to correct position
        self.lscore.pendown()
        self.update_score(self.lscore, self.Lscore)

    def radd(self):
        self.Rscore += 1
        self.rscore.clear()  # Clear the previous score
        self.rscore.penup()
        self.rscore.goto(100, 250)  # Set to correct position
        self.rscore.pendown()
        self.update_score(self.rscore, self.Rscore)
