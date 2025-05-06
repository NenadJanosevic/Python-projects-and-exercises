import time
from Snake import Snake
import turtle as t
from food import Food
from scoreboard import Scoreboard

screen = t.Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("black")
screen.title("Snek.io game")
screen.tracer(0)

snake = Snake()
food = Food()
text = Scoreboard() 


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        text.score += 1
        text.update_score()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        text.reset()
        snake.reset()
        
    for seqment in snake.segments[1:]:
        if snake.head.distance(seqment) < 10: # ako je glava blizu bilo kog dela to jest u blizin od 10 piksela 
            text.reset()
            snake.reset()
    
    
     






screen.exitonclick()