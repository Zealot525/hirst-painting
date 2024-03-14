# # getting the colors from hirst paintings
# import colorgram

# rgb_colors = []
# colors = colorgram.extract('hirst-painting/painting.jpg',45)
# for i in colors:
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     rgb_colors.append(tuple([r,g,b]))

# print(rgb_colors)

from turtle import Turtle, Screen
import random

rgb_colors = [(141, 174, 201), (22, 30, 46), (34, 106, 151), (207, 159, 112), (227, 211, 100), (141, 28, 61), (173, 49, 83), (211, 71, 99), (12, 163, 193), (193, 137, 169), (63, 168, 114), (136, 91, 74), (32, 60, 111), (115, 180, 110), (223, 79, 48), (191, 184, 43), 
(172, 209, 178), (7, 94, 111), (238, 205, 4), (78, 31, 64), (50, 144, 111), (221, 174, 192), (229, 171, 162), (143, 208, 230), (186, 184, 212), (108, 38, 36), (116, 121, 154), (84, 27, 26), (9, 103, 104)]

jason = Turtle()
my_screen = Screen()
my_screen.setworldcoordinates(-1, -1, my_screen.window_width() - 1, my_screen.window_height() - 1)
my_screen.colormode(255)
y_position = 30
x_position = 100
blank_space = 50
jason.teleport(x_position, y_position)
jason.speed(0)
jason.pu()
jason.hideturtle()


def draw_row():
    for i in range(10):
        color_choice = random.choice(rgb_colors)
        jason.dot(20,color_choice)
        jason.fd(blank_space)

def draw_painting():
    global y_position
    for i in range(10):
        draw_row()
        y_position += blank_space
        jason.teleport(x_position, y_position)

draw_painting()

my_screen.exitonclick()
