from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,positons):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.turtlesize(stretch_wid = 5, stretch_len = 1)
        self.penup()
        self.goto(positons)
    
    def up(self):
        y_up = self.ycor() + 20
        self.goto(self.xcor(),y_up)

    def down(self):
        y_down = self.ycor() - 20
        self.goto(self.xcor(),y_down)




