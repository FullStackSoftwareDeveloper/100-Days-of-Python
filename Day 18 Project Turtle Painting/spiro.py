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

def draw_spiro(size_of_gap):
    for i in range(int(360/size_of_gap)):
        turtle.color(random_color())
        turtle.circle(100)
        turtle.right(i+size_of_gap)

draw_spiro(5)

screen.exitonclick()