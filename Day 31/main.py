from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
currentcard = {}
to_learn = {}
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")  # to convert the data into dictionary


def nextcard():
    global currentcard, fliptimer
    window.after_cancel(fliptimer)
    currentcard = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_text, text=currentcard["French"])
    canvas.itemconfig(card_background, image=card_front_image)
    fliptimer = window.after(3000, func=flip_card)


def flip_card():
    # defining the flip card function
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_text, text=currentcard["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_image)


def isknown():
    to_learn.remove(currentcard)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    nextcard()


window = Tk()
window.title("Flashcard")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
fliptimer = window.after(3000, func=flip_card)


canvas = Canvas(width=800, height=526)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front_image)
canvas.grid(row=0, column=0)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_text = canvas.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

crossimage = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=crossimage, highlightthickness=0, command=nextcard)
unknown_button.config(highlightthickness=0)
unknown_button.grid(row=1, column=0)

checkimage = PhotoImage(file="images/right.png")
known_button = Button(image=checkimage, highlightthickness=0, command=isknown)
known_button.grid(row=1, column=1)


nextcard()
window.mainloop()
