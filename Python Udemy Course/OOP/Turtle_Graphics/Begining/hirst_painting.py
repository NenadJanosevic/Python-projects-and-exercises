# import colorgram

# rgb_colors = []
# # Extract 6 colors from an image.
# colors = colorgram.extract('python_paining.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)    

# print(rgb_colors)
import turtle
import random

turtle.colormode(255)
color_list = [(140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), (232, 165, 190), (233, 174, 161), (141, 213, 224), (191, 191, 193), (160, 211, 182), (105, 46, 100), (8, 
117, 39)]
tim = turtle.Turtle()
tim.penup()
tim.goto(-200,-200 )
def color_random():
    color = tim.pencolor(random.choice(color_list))

y = -160
while True:  
    for _ in range(10):
        color_random()
        tim.dot(35)
        tim.penup()
        tim.forward(40)
        tim.pendown()
    
    tim.teleport(-200,y)
    y += 40
    if y == 240:
        tim.hideturtle()
        break

screen = turtle.Screen()
screen.exitonclick()
