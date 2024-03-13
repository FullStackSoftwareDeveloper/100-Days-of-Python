import turtle as t
from turtle import Screen
import random

turtle = t.Turtle()
screen = Screen()

t.colormode(255)
turtle.speed("fastest")

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb

def draw_line():
    for i in range(24):
        turtle.color(random_color())
        turtle.dot(20)
        turtle.penup()
        turtle.fd(50)
        turtle.pendown()
        turtle.dot(20)

# 600 by 500 window
bottom = -500
for i in range(21):
    turtle.teleport(-600, bottom)
    draw_line()
    bottom += 50

screen.exitonclick()