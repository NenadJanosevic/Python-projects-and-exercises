import time
from turtle import Screen,Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up,"Up")

car_Manager = CarManager()
scoreboard = Scoreboard()
scoreboard.uppdate_score()
game_is_on = True
while game_is_on:
    time.sleep(0.17)
    screen.update()
    for car in car_Manager.cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False
        if player.ycor() > 290:
            player.goto(0, -280) 
            scoreboard.score += 1
            car_Manager.increas_Speed()
            car_Manager.SPAWN_CHANCE += 1
            scoreboard.uppdate_score()
    car_Manager.new_cars()
    car_Manager.car_move()
    
screen.exitonclick()