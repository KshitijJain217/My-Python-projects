#use the below code to extract color from any given image 👇
# import colorgram
#
# rgb_colors =[]
# colors = colorgram.extract('colorful.png', 8)
# for color in colors:
#     # rgb_colors.append(color.rgb)
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

#use the below code to create a dot painting 👇
color_list = [(254, 253, 253), (101, 190, 171), (100, 164, 209), (207, 137, 182), (213, 230, 240), (56, 179, 154),
              (49, 124, 170), (187, 222, 211)]
import random
import turtle
turtle.colormode(255)
timmy = turtle.Turtle()
timmy.speed("fastest")
timmy.penup()
timmy.hideturtle()

timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    timmy.dot(20, random.choice(color_list))
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)

screen = turtle.Screen()
turtle.exitonclick()

