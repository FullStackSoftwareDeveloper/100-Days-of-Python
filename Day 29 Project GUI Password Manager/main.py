import tkinter
from tkinter import messagebox
import random

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
        with open("data.txt", mode="a") as data:
            data.write(f"{entry1.get()} | {entry2.get()} | {entry3.get()}\n")
        entry1.delete(0, tkinter.END)
        entry2.delete(0, tkinter.END)
        entry3.delete(0, tkinter.END)
        messagebox.showinfo(title="Info", message="Successfully added")

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
entry1 = tkinter.Entry(width=35)
entry1.grid(column=2, row=2, columnspan=2)
entry1.focus()

label2 = tkinter.Label(text="Email/Username")
label2.grid(column=1, row=3)
entry2 = tkinter.Entry(width=35)
entry2.grid(column=2, row=3, columnspan=2)

label3 = tkinter.Label(text="Password")
label3.grid(column=1, row=4)
entry3 = tkinter.Entry(width=20)
entry3.grid(column=2, row=4)

button1 = tkinter.Button(text="Generate Password", command=generate)
button1.grid(column=3, row=4)
button2 = tkinter.Button(width=30, text="Add", command=save)
button2.grid(column=2, row=5, columnspan=2)

window.mainloop()