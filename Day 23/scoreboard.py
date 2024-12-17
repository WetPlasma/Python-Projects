from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(
        self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True
    ) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.level = int(1)
        self.hideturtle()
        self.penup()
        self.goto(-200, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def inclevel(self):

        self.level += 1
        self.update()

    def gameover(self):
        self.goto(0, 0)
        self.write(f"Game Over", align="center", font=FONT)
