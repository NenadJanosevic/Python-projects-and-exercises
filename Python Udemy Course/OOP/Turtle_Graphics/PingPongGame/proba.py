import turtle
import random

NUBMERS_X = (-740, 740) 
Y = random.randint(-600, 600)
X = random.choice(NUBMERS_X) 
turtle.bgcolor("black")
turtle.shape("circle")
turtle.color("white")
turtle.penup()
turtle.speed(1)
turtle.setup(width = 800,height = 600)
turtle.goto(X,Y)
turtle.forward(800)



screen = turtle.Screen()
screen.exitonclick()