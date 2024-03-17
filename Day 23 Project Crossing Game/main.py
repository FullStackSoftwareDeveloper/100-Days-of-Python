from turtle import Screen, Turtle
import random
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

turtle = Turtle()
turtle.shape("turtle")
turtle.penup()
turtle.teleport(0, -280)
turtle.setheading(90)

def move():
    turtle.fd(10)

screen.listen()
screen.onkey(move, "Up")

list_cars = []
for i in range(20):
    car = Turtle()
    list_cars.append(car)
    car.shape("square")
    car.shapesize(1, 2)
    car.penup()
    car.teleport(random.randint(-200, 200), random.randint(-200, 200))

while True:
    for car in list_cars:
        car.fd(10)
        if car.xcor() > 300:
            car.teleport(-300, random.randint(-200, 200))
        if car.distance(turtle) < 15:
            turtle.teleport(0, -280)
    if turtle.ycor() > 280:
        print("You win!")
        break
    time.sleep(0.2)
    screen.update()

screen.exitonclick()