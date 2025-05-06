# from turtle import Turtle,Screen


# tim = Turtle()
# tim.shape("turtle")
# tim.color("red")
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

# screen = Screen()
# screen.exitonclick()

# import turtle as t
# tim = t.Turtle
# import heroes
# import villains

# print(villains.gen())
# print(heroes.gen())

# import turtle

# tim = turtle.shape("turtle")
# tim = turtle.color("Green")
# tim = turtle.penup()   
# tim = turtle.goto(-500, 0)  
# tim = turtle.pendown() 
# for _ in range(24):
#     tim = turtle.forward(20)
#     tim = turtle.penup()
#     tim = turtle.forward(20)
#     tim = turtle.pendown()
    


# screen = turtle.Screen()
# screen.exitonclick()

# import turtle as t

# tim = t.shape("turtle")
# tim = t.pencolor("red")
# for _ in range(3):
#     tim = t.forward(100)
#     tim = t.right(120)

# tim = t.shape("turtle")
# tim = t.pencolor("blue")
# for _ in range(4):
#     tim = t.forward(100)
#     tim = t.right(90)

# tim = t.shape("turtle")
# tim = t.pencolor("Black")
# for _ in range(5):
#     tim = t.forward(100)
#     tim = t.right(72)

# tim = t.shape("turtle")
# tim = t.pencolor("blue")
# for _ in range(7):
#     tim = t.forward(100)
#     tim = t.right(60)

# tim = t.shape("turtle")
# tim = t.pencolor("Green")
# for _ in range(8):
#     tim = t.forward(100)
#     tim = t.right(45)
# screen = t.Screen()
# screen.exitonclick()

# import turtle 
# import random

# tim = turtle.Turtle()
# tim.pensize(10)
# def random_move():
#     tim.speed("fastest")
#     moves = [
#         lambda: tim.forward(25),
#         lambda: tim.right(90),
#         lambda: tim.right(180),
#         lambda: tim.backward(25)
#     ]
#     random.choice(moves)() 
#     random_color()
#     screen.ontimer(random_move, 200)
    
# def random_color():
#     colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
#     tim.pencolor(random.choice(colors))

    
# screen = turtle.Screen()
# screen.tracer(0)
# random_move()
# screen.update()
# screen.exitonclick()

import turtle
import random

turtle.colormode(255)
turtle.bgcolor("black")
tim = turtle.Turtle()
tim.speed(0)
tim.pencolor("251")
tim.hideturtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

for _ in range(75):
    # tim.color(random_color())
    tim.circle(100)
    tim.right(5)
for _ in range(75):
    # tim.color(random_color())
    tim.circle(150)
    tim.right(5)
for _ in range(75):
    # tim.color(random_color())
    tim.circle(200)
    tim.right(5)
for _ in range(75):
    # tim.color(random_color())
    tim.circle(300)
    tim.right(5)  

exit = turtle.Screen()
exit.exitonclick()
