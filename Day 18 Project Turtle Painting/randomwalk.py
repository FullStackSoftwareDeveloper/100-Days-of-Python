import turtle as t
from turtle import Screen
import random

turtle = t.Turtle()
screen = Screen()

t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

turn_radius = [0, 90, 180, 270]
direction = ["left", "right"]

turtle.pensize(15)

for i in range(100):
    turtle.color(random_color())
    turtle.fd(30)
    angle = random.choice(turn_radius)
    turn = random.choice(direction)
    if turn == "left":
        turtle.left(angle)
    else:
        turtle.right(angle)

screen.exitonclick()