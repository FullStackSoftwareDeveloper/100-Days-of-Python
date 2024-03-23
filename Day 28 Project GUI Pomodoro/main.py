import math
import tkinter

window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50)

# Countdown
rep = 0
temp = None
def countdown(count):
    global rep
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    if minutes == 0 and int(seconds) < 10 and int(seconds) > 0:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer, text=f"{minutes}:{seconds}")
    if count > 0:
        global temp
        temp = window.after(1000, countdown, count-1)
    else:
        start_timer()
        mark = ""
        for i in range(math.floor(rep/2)):
            mark += " V "
        checkmark.config(text=mark)

def start_timer():
    global rep
    rep += 1
    if rep % 8 == 0:
        countdown(30*60)
        label.config(text="Long Break", font=("Arial", 30, "bold"))
    elif rep % 2 == 0:
        countdown(5*60)
        label.config(text="Short Break", font=("Arial", 30, "bold"))
    else:
        countdown(25*60)
        label.config(text="Work", font=("Arial", 30, "bold"))

def reset_timer():
    window.after_cancel(temp)
    canvas.itemconfig(timer, text="00:00")
    label.config(text="Timer", font=("Arial", 30, "bold"))
    checkmark.config(text="")
    global rep
    rep = 0

# UI Setup
label = tkinter.Label(text="Timer", font=("Arial", 30, "bold"))
label.grid(column=2, row=1)
checkmark = tkinter.Label(text="")
checkmark.grid(column=2, row=3)

canvas = tkinter.Canvas(width=200, height=224)
tomato = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(102, 114, image=tomato)
timer = canvas.create_text(102, 130, text="00:00", fill="white", font=("Arial", 30, "bold"))
canvas.grid(column=2, row=2)

start = tkinter.Button(text="Start", command=start_timer)
start.grid(column=1, row=3)
reset = tkinter.Button(text="Reset", command=reset_timer)
reset.grid(column=3, row=3)

window.mainloop()