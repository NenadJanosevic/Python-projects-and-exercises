import turtle
import random

# Create turtle object
tim = turtle.Turtle()
tim.pensize(10)

def random_move():
    moves = [
        lambda: tim.forward(25),
        lambda: tim.right(90),
        lambda: tim.right(180),
        lambda: tim.backward(25)
    ]
    random.choice(moves)()  
    random_color()
    screen.ontimer(random_move, 200)  # Repeat after 200ms

def random_color():
    colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "brown", "black", "white"]
    tim.pencolor(random.choice(colors))

# Set up screen
screen = turtle.Screen()
screen.tracer(0)  # Speeds up drawing
random_move()  # Start the loop
screen.update()  # Update screen
screen.exitonclick()  # Now this will work!
