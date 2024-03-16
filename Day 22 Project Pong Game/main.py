import turtle as t
from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.tracer(0)

#turtle = t.Turtle()
#turtle.color("white")
#turtle.shape("square")
#turtle.shapesize(30, 0.5)

paddle = Paddle()
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(paddle.move_up_right, "Up")
screen.onkey(paddle.move_down_right, "Down")
screen.onkey(paddle.move_up_left, "w")
screen.onkey(paddle.move_down_left, "s")
while True:
    time.sleep(0.1)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    if ball.distance(paddle.paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle.paddle_left) < 30 and ball.xcor() > -340:
        ball.bounce2()
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.return_home()
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.return_home()

screen.exitonclick()