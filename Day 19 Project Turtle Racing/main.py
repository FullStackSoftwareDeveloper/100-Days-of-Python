import turtle as t
from turtle import Screen

turtle = t.Turtle()
screen = Screen()

def f():
    turtle.fd(50)

def b():
    turtle.bk(50)

def l():
    turtle.lt(45)

def r():
    turtle.rt(45)

def cl():
    t.resetscreen()

screen.onkey(f, "w")
screen.onkey(b, "s")
screen.onkey(l, "a")
screen.onkey(r, "d")
screen.onkey(cl, "c")
screen.listen()

screen.exitonclick()