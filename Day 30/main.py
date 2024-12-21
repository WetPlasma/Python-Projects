import tkinter as tk
from tkinter import messagebox
import PasswordGenerator
import json
import searchs


def writeup(website, email, password):
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(
            title="Oops", message="Please make sure you haven't left any fields empty."
        )
    else:
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
        except FileNotFoundError:
            data = {}

        # Updating old data with new data
        data.update(new_data)

        with open("data.json", "w") as data_file:
            # Saving updated data
            json.dump(data, data_file, indent=4)

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


def passwords():
    password = PasswordGenerator.generate_hard_password()
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)


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

search_button = tk.Button(root, text="Search", command=lambda: search_website())
search_button.grid(row=1, column=2)

add_button = tk.Button(
    root,
    text="Add",
    width=36,
    command=lambda: writeup(
        website_entry.get(), email_entry.get(), password_entry.get()
    ),
)
add_button.grid(row=4, column=1, columnspan=2)


# Function to handle search
def search_website():
    website = website_entry.get()
    result = searchs.search(website)

    # Show result in a messagebox
    if isinstance(
        result, dict
    ):  # If a dictionary is returned, display the email and password
        email = result.get("email", "Not found")
        password = result.get("password", "Not found")
        messagebox.showinfo(
            title="Website Found", message=f"Email: {email}\nPassword: {password}"
        )
    else:
        messagebox.showinfo(title="Search Result", message=result)


root.mainloop()
