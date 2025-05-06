from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("black")
        self.hideturtle()
        self.goto(-200,260)
    
    def game_over(self):
        self.goto(0,0)
        self.write (arg= "Game over", move = False, align = "center", font=("Courier", 24, "normal"))

    def uppdate_score(self):
        self.clear()
        self.write (arg= f"score = {self.score}", move = False, align = "center", font=("Courier", 24, "normal"))
        