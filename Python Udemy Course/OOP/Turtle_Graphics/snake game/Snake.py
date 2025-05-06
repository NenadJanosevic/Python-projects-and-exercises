# import turtle as t

# screen = t.Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("Snek.io game")
# t.hideturtle()
# t.pencolor("white")
# def Snek_Body():
#     t.fillcolor("white")
#     t.begin_fill()
#     x = 0
#     turtles = []
#     while True:
#         if len(turtles) > 3:
#             break
#         for _ in range(4):
#             new_turtles = t.Turtle()
#             t.forward(20)
#             t.right(90)
#         turtles.append(new_turtles)
#         t.teleport(x,0)
#         x += -20
#     t.end_fill()

# Snek_Body()

# import time
# import turtle as t

# screen = t.Screen()
# screen.setup(width = 600, height = 600)
# screen.bgcolor("black")
# screen.title("Snek.io game")
# screen.tracer(0)
# positions = [(0,0), (-20,0), (-40,0)]
# seqments = []


# for position in positions:
#     new_turtle = t.Turtle("square")
#     new_turtle.color("white")
#     new_turtle.penup( )
#     new_turtle.goto(position)
#     seqments.append(new_turtle)

# while True:
#     screen.update()
#     time.sleep(0.1)
#     for seg_num in range(len(seqments)-1 , 0, -1):
#         new_x = seqments[seg_num - 1].xcor()
#         new_y = seqments[seg_num - 1].ycor()    
#         seqments[seg_num].goto(new_x,new_y)
#     seqments[0].forward(20)

# screen.exitonclick()
import turtle as t

STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
class Snake:
    def __init__(self):
        self.segments = []
        self.creat_snake()
        self.head = self.segments[0]

    def creat_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            

    def add_segment(self,position):
        new_turtle = t.Turtle("square")
        new_turtle.color("white")
        new_turtle.penup( )
        new_turtle.goto(position)
        self.segments.append(new_turtle)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.creat_snake()
        self.head = self.segments[0]        

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
        for seg_num in range(len(self.segments)-1 , 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()    
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self): 
        if self.head.heading() != 270: 
            self.head.setheading(90) 
    def down(self):
        if self.head.heading() != 90: 
            self.head.setheading(270)
    def left(self):
        if self.head.heading() != 0: 
            self.head.setheading(180)
    def right(self):
        if self.head.heading() != 180: 
            self.head.setheading(0)  
 

         
    
