# hirstPainting.py
#
# Python Bootcamp Day 18 - Hirst Painting
# Usage:
#      Create a Hirst influenced drawing using the Turtle module.
#
# Marceia Egler Nov 1, 2021

from turtle import Turtle, Screen
import random
import colorgram

colors = colorgram.extract('image.jpg', 30)
bob = Turtle()


def change_color():
    Screen().colormode(255)
    first_color = colors[random.randrange(0,30)]
    r = first_color.rgb[0]
    g = first_color.rgb[1]
    b = first_color.rgb[2]

    return r, g, b


bob.speed("fastest")
bob.penup()
x = -200
y = -200
bob.goto(x, y)
bob.pendown()


def draw(dots):
    for _ in range(dots):
        bob.hideturtle()
        bob.dot(20, change_color())
        bob.penup()
        bob.fd(50)
        bob.pendown()


def draw_grid(rows, starting_y):
    for _ in range(rows):
        draw(10)
        bob.penup()
        starting_y += 50
        bob.goto(x, starting_y)


draw_grid(10, y)



screen = Screen()
screen.exitonclick()
