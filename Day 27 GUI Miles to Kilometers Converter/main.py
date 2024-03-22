import tkinter

window = tkinter.Tk()
window.title("Miles to Km")
window.minsize(250, 100)

label1 = tkinter.Label(text="Miles")
label1.grid(column=2, row=0)

label2 = tkinter.Label(text="is equal to")
label2.grid(column=0, row=2)

label3 = tkinter.Label(text="0")
label3.grid(column=1, row=2)

label4 = tkinter.Label(text="Km")
label4.grid(column=2, row=2)

user = tkinter.Entry()
user.grid(column=1, row=0)

def convert():
    converted = float(user.get())*1.609344
    label3.config(text=round(converted, 2))

button = tkinter.Button(text="Convert", command=convert)
button.grid(column=1, row=3)

window.mainloop()