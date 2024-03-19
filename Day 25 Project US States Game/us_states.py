import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

data = pandas.read_csv("50_states.csv")

list_states = data["state"].tolist()

score = 0
while True:
    answer = screen.textinput("Guess the state", "Pick a state")
    for state in list_states:
        if state == answer.title():
            score += 1
            turtle_state = turtle.Turtle()
            turtle_state.hideturtle()
            x_cor = int(data[data["state"] == state].x.iloc[0])
            y_cor = int(data[data["state"] == state].y.iloc[0])
            turtle_state.teleport(x_cor, y_cor)
            turtle_state.write(state, align="center", font=("Arial", 9, "normal"))
            print(f"{score}/50")
    if score == 50:
        break