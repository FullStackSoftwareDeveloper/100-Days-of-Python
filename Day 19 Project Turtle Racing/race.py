import turtle as t
from turtle import Screen
import random

turtle1 = t.Turtle()
turtle2 = t.Turtle()
turtle3 = t.Turtle()
screen = Screen()
screen.setup(1275, 1000)
user = screen.textinput("Pick a turtle", "Winning color: ")

turtle1.shape("turtle")
turtle2.shape("turtle")
turtle3.shape("turtle")
turtle1.color("red")
turtle2.color("green")
turtle3.color("blue")

turtle1.teleport(-600, -100)
turtle2.teleport(-600, 0)
turtle3.teleport(-600, 100)
while True:
    if turtle1.xcor() > 600:
        print("Red turtle wins")
        if user == "red":
            print(f"You bet {user}, bet won!")
        else:
            print(f"You bet {user}, bet lost!")
        break
    if turtle2.xcor() > 600:
        print("Green turtle wins")
        if user == "green":
            print(f"You bet {user}, bet won!")
        else:
            print(f"You bet {user}, bet lost!")
        break
    if turtle3.xcor() > 600:
        print("Blue turtle wins")
        if user == "blue":
            print(f"You bet {user}, bet won!")
        else:
            print(f"You bet {user}, bet lost!")
        break
    turtle1.fd(random.randint(1,20))
    turtle2.fd(random.randint(1,20))
    turtle3.fd(random.randint(1,20))

screen.exitonclick()