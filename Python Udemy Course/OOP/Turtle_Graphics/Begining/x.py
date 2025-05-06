# import turtle
# import random

# # Setup Turtle and Color Mode
# turtle.colormode(255)
# color_list = [(140, 49, 106), (164, 169, 38), (244, 80, 56), (228, 115, 163), 
#               (3, 143, 56), (215, 234, 231), (241, 65, 140), (1, 143, 184), 
#               (162, 55, 51), (50, 203, 226), (254, 230, 0), (20, 166, 126), 
#               (244, 223, 49), (210, 231, 234), (171, 186, 177), (27, 197, 220), 
#               (232, 165, 190), (233, 174, 161), (141, 213, 224), (191, 191, 193), 
#               (160, 211, 182), (105, 46, 100), (8, 117, 39)]

# tim = turtle.Turtle()
# tim.speed("fastest")  # Speeds up drawing
# tim.penup()
# tim.goto(-200, -200)

# # Function to Set a Random Color
# def color_random():
#     tim.pencolor(random.choice(color_list))  # Just set the color, no return needed

# # Function to Draw a Grid of Dots
# def draw_dots():
#     y = -200  # Start at the bottom
#     for _ in range(10):  # 10 rows
#         tim.goto(-200, y)
#         for _ in range(10):  # 10 dots per row
#             color_random()
#             tim.dot(35)
#             tim.penup()
#             tim.forward(40)  # Move right for spacing
#             tim.pendown()
#         y += 40  # Move up for next row

# draw_dots()  # Call the function to start drawing

# turtle.done()

# import turtle


# turtle.Turtle()
# turtle.hideturtle()
# turtle.penup()
# turtle.goto(-290,290)
# turtle.write(arg= f"Scoreboard ", move = False, align = "right")

# screen = turtle.Screen()
# screen.exitonclick()