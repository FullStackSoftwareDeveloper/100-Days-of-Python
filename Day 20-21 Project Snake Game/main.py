import turtle as t
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

counter = 0
while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.turtle1.distance(food) < 15:
        scoreboard.clear()
        counter += 1
        food.refresh()
        scoreboard.write(f"Score: {counter}", False, align="center", font=("Arial", 12, "normal"))
    if snake.turtle1.xcor() > 280 or snake.turtle1.xcor() < -280 or snake.turtle1.ycor() > 280 or snake.turtle1.ycor() < -280:
        print("Game Over")
        break

screen.exitonclick()