import turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

turtle.bgcolor("black")
turtle.title("Ping Pong")
turtle.setup(width = 800,height = 600)
screen = turtle.Screen()
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up,"Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up,"w")
screen.onkey(l_paddle.down,"s")

while True:
    time.sleep(ball.move_speed) 
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > -320: 
        ball.bounce_x()
    
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
       
    
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
       




screen.exitonclick()