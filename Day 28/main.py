from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- UI SETUP ------------------------------- #
def start_timer():
    countdown(2 * 60)


def countdown(count):
    if count >= 0:
        window.after(1000, countdown, count - 1)
        count_min = math.floor(count / 60)
        count_sec = count % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        canvas.itemconfig(timertext, text=f"{count_min}:{count_sec}")
        print(count)


window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)  # Added background color for better UI
fg = GREEN

# Load image
picture = PhotoImage(file="tomato.png")  # Ensure the correct path to the image file
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(101, 112, image=picture)
timertext = canvas.create_text(
    103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold")
)
canvas.grid(column=1, row=1)
start = Button(text="Start", command=start_timer)
start.grid(row=2, column=0)
reset = Button(text="Reset")
reset.grid(row=2, column=2)
topictext = Label(text="Timer", foreground=fg, font=(FONT_NAME, 35, "bold"))
topictext.grid(row=0, column=1)
check = "✓"
cecktext = Label(text=f"{check}", foreground=fg, font=(FONT_NAME, 20, "bold"))
cecktext.grid(row=3, column=1)

window.mainloop()
