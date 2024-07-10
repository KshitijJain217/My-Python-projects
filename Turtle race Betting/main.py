import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make Your Bets.", prompt="Which turtle will win the race? Enter a color:")
colors = ["red", "orange", "yellow", "blue", "green", "purple" ]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = turtle.Turtle(shape= "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You Win!!! The {winning_color} turtle is the Winner!")
            else:
                print(f"You Lose! The {winning_color} turtle is the Winner!")
                
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()