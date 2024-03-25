import tkinter
from tkinter import messagebox
import random
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
list_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
              "-", "!", "?", "*"]
def generate():
    password = ""
    entry3.delete(0, tkinter.END)
    for i in range(8):
        password += random.choice(list_chars)
    entry3.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if entry1.get() == "" or entry2.get() == "" or entry3.get() == "":
        messagebox.showinfo(title="Error", message="Missing fields")
    else:
        json_dict = {
            entry1.get(): {
                "email": entry2.get(),
                "password": entry3.get(),
            }
        }
        try:
            with open("data.json", mode="r") as data_file:
                data = json.load(data_file)
                data.update(json_dict)
        except FileNotFoundError:
            with open("data.json", mode="w") as data_file:
                json.dump(json_dict, data_file, indent=4)
        else:
            with open("data.json", mode="w") as data_file:
                json.dump(data, data_file, indent=4)
        entry1.delete(0, tkinter.END)
        entry2.delete(0, tkinter.END)
        entry3.delete(0, tkinter.END)
        messagebox.showinfo(title="Info", message="Successfully added")

def search():
    try:
        with open("data.json", mode="r") as data_file:
            data = json.load(data_file)
            first_dict = data.get(entry1.get())
            messagebox.showinfo(title="Search", message=f"Email: {first_dict.get("email")}\nPassword: {first_dict.get("password")}")
    except AttributeError:
        messagebox.showinfo(title="Search", message=f"No info recorded in database")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tkinter.Canvas(width=200, height=200)
logo = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=2, row=1)

label1 = tkinter.Label(text="Website")
label1.grid(column=1, row=2)
entry1 = tkinter.Entry(width=25)
entry1.grid(column=2, row=2)
entry1.focus()

label2 = tkinter.Label(text="Email/Username")
label2.grid(column=1, row=3)
entry2 = tkinter.Entry(width=25)
entry2.grid(column=2, row=3)

label3 = tkinter.Label(text="Password")
label3.grid(column=1, row=4)
entry3 = tkinter.Entry(width=25)
entry3.grid(column=2, row=4)

button1 = tkinter.Button(width=20, text="Generate Password", command=generate)
button1.grid(column=3, row=4)
button2 = tkinter.Button(width=20, text="Add", command=save)
button2.grid(column=2, row=5)
button3 = tkinter.Button(width=20, text="Search", command=search)
button3.grid(column=3, row=2)

window.mainloop()