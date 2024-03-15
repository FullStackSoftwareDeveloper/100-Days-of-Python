import turtle as t

class Snake:
    def __init__(self):
        self.turtle1 = t.Turtle()
        self.turtle2 = t.Turtle()
        self.turtle3 = t.Turtle()
        self.turtle1.shape("square")
        self.turtle1.color("white")
        self.turtle1.penup()
        self.turtle2.shape("square")
        self.turtle2.color("white")
        self.turtle2.penup()
        self.turtle3.shape("square")
        self.turtle3.color("white")
        self.turtle3.penup()
        self.turtle2.teleport(-20, 0)
        self.turtle3.teleport(-40, 0)

    def move(self):
        self.turtle3.teleport(self.turtle2.xcor(), self.turtle2.ycor())
        self.turtle2.teleport(self.turtle1.xcor(), self.turtle1.ycor())
        self.turtle1.fd(20)

    def up(self):
        self.turtle1.setheading(90)

    def down(self):
        self.turtle1.setheading(270)

    def left(self):
        self.turtle1.setheading(180)

    def right(self):
        self.turtle1.setheading(0)