import turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
tim = turtle.Turtle()
x = []
while True:
    for colors in COLORS:
        new_turtle = turtle.Turtle("turtle")
        new_turtle.penup()
        new_turtle.color(colors)
        new_turtle.goto(random.randint(-290,290), random.randint(-250,250))


screen = turtle.Screen()
screen.exitonclick()
    