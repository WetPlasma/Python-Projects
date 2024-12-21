import tkinter as tk
from tkinter import messagebox
import PasswordGenerator


def writeup(*args):

    with open("data.txt", "a") as writer:
        if len(args[0]) == 0 or len(args[1]) == 0 or len(args[2]) == 0:
            messagebox.showinfo(title="oops", message="fill all details")
        else:
            messagebox.askokcancel(title=f"{args[0]}", message="you want to confirm?")
            writer.write(f"{args[0]}|{args[1]}|{args[2]}\n")


def passwords():
    password_entry.insert(0, PasswordGenerator.generate_hard_password())


# Create the main application window
root = tk.Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)

# Logo
canvas = tk.Canvas(root, width=200, height=200)
logo_img = tk.PhotoImage(file="logo.png")  # Replace with your logo file
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
website_label = tk.Label(root, text="Website:")
website_label.grid(row=1, column=0)

email_label = tk.Label(root, text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = tk.Label(root, text="Password:")
password_label.grid(row=3, column=0)

# Entries
website_entry = tk.Entry(root, width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_entry = tk.Entry(root, width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "example@example.com")

password_entry = tk.Entry(root, width=21)
password_entry.grid(row=3, column=1)

# Buttons
generate_password_button = tk.Button(root, text="Generate Password", command=passwords)
generate_password_button.grid(row=3, column=2)

add_button = tk.Button(
    root,
    text="Add",
    width=36,
    command=lambda: writeup(
        website_entry.get(), email_entry.get(), password_entry.get()
    ),
)
add_button.grid(row=4, column=1, columnspan=2)

root.mainloop()
