from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.title("The Snake Game")
screen.bgcolor("black")

screen.tracer(0)

# a single turtle is 20x20 in width and height
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # this is to make sure the animation is smooth.
    screen.update()
    time.sleep(0.1)
    snake.move()

#     detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

#     detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

#     detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()