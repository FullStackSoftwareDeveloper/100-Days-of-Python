import tkinter
import pandas
import random

window = tkinter.Tk()
window.config(padx=50, pady=50)

canvas = tkinter.Canvas(width=800, height=600)
card_front = tkinter.PhotoImage(file="./images/card_front.png")
canvas.create_image(400, 300, image=card_front)
canvas.grid(column=1, row=1, columnspan=3)

right = 0
wrong = 0

def word():
    with open("./data/french_words.csv") as data_file:
        data = pandas.read_csv(data_file)
        data_dict = data.to_dict(orient="records")
        choice = random.choice(data_dict)
        label_title.config(text="French")
        label_word.config(text=choice["French"])

    def flip_card():
        label_title.config(text="English")
        label_word.config(text=choice["English"])

    window.after(3000, func=flip_card)

def wrong_word():
    global right
    global wrong
    wrong += 1
    print(f"I didn't know this word - Right: {right} Wrong: {wrong}")

def right_word():
    global right
    global wrong
    right += 1
    print(f"I knew this word - Right: {right} Wrong: {wrong}")

wrong_img = tkinter.PhotoImage(file="./images/wrong.png")
button_wrong = tkinter.Button(image=wrong_img, padx=50, pady=50, command=wrong_word)
button_wrong.grid(column=1, row=2)
right_img = tkinter.PhotoImage(file="./images/right.png")
button_word = tkinter.Button(text="Word", padx=25, pady=10, command=word)
button_word.grid(column=2, row=2)
button_right = tkinter.Button(image=right_img, padx=50, pady=50, command=right_word)
button_right.grid(column=3, row=2)

label_title = tkinter.Label(text="Title", font=("Arial", 40, "italic"))
label_title.place(x=350, y=150)
label_word = tkinter.Label(text="Word", font=("Arial", 60, "bold"))
label_word.place(x=300, y=300)

window.mainloop()