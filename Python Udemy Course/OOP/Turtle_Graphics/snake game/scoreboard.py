from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self,):
        super().__init__()
        self.score = 0
        with open(r"C:\Users\PC\Python Udemy Course\OOP\Turtle_Graphics\snake game\data.txt" ,"r") as file:
            self.high_score = int(file.read())
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-280,250)
        self.update_score() 

    def update_score(self):
        self.clear()
        self.write (arg= f"Score = {self.score}  High socre = {self.high_score}", move = False, align = "left", font=("Arial", 16, "normal"))
    
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score 
            with open(r"C:\Users\PC\Python Udemy Course\OOP\Turtle_Graphics\snake game\data.txt" ,"w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
    
    
    
    
    
    # def game_over(self):
    #     self.goto(0,0)
    #     self.write (arg= "Game over", move = False, align = "center", font=("Arial", 16, "normal"))

    # def increase_score(self):
    #     if snake.head.distance(food) < 15:
    #         self.score += 1
    #         self.update_score()



    

        
