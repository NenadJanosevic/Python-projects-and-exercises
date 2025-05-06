import turtle
import random


game_on = False 
screen = turtle.Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "What is your bet,ser", prompt = "Whic turtle collor will win? Enter a color:")
print(user_bet)
colors = ["blue", "red", "orange", "purple"]
x = -235
y = -150
turtles = []
for color in colors:
    new_turtle = turtle.Turtle("turtle")
    turtles.append(new_turtle)
    new_turtle.penup()
    new_turtle.color(color)
    new_turtle.goto(x, y)
    y += 100
if user_bet:
    game_on = True 
while game_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_on = False 
            if user_bet == turtle.pencolor():
                print(f"You won the winner is {turtle.pencolor()}")
            else:
                print(f"You lost the winner is {turtle.pencolor()}")
        turtle.forward(random.randint(0,10))
        




screen.exitonclick()