import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed = []

while len(guessed) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed)}/50 Guess the State",
        prompt="What's another state's name?",
    ).title()
    if answer_state == "Exit":
        missingstates = []
        for state in states:
            if state not in guessed:
                missingstates.append(state)
        newdata = pandas.DataFrame(missingstates)
        newdata.to_csv("learnthese.csv")
        break
    if answer_state in states:
        guessed.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        statedata = data[data.state == answer_state]
        t.goto(int(statedata.x), int(statedata.y))
        t.write(answer_state)


print(answer_state)
