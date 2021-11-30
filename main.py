# Programmer: Sourav Sharma

import turtle as turtle_module
import colorgram
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
tim.speed(0)
tim.penup()
tim.hideturtle()

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    color_tuple = (r, g, b)
    rgb_colors.append(color_tuple)

# Copied from output from above function

color_list = [(248, 248, 245), (240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80), (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103), (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179), (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72), (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34), (71, 10, 28)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()

