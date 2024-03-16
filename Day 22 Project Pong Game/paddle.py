from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.paddle_right = Turtle()
        self.paddle_right.penup()
        self.paddle_right.color("white")
        self.paddle_right.shape("square")
        self.paddle_right.shapesize(5, 1)
        self.paddle_right.teleport(350, 0)
        self.paddle_left = Turtle()
        self.paddle_left.penup()
        self.paddle_left.color("white")
        self.paddle_left.shape("square")
        self.paddle_left.shapesize(1, 5)
        self.paddle_left.setheading(90)
        self.paddle_left.teleport(-350, 0)

    def move_up_right(self):
        new_y = self.paddle_right.ycor() + 30
        self.paddle_right.sety(new_y)

    def move_down_right(self):
        new_y = self.paddle_right.ycor() - 30
        self.paddle_right.sety(new_y)

    def move_up_left(self):
        new_y = self.paddle_left.ycor() + 30
        self.paddle_left.sety(new_y)

    def move_down_left(self):
        new_y = self.paddle_left.ycor() - 30
        self.paddle_left.sety(new_y)