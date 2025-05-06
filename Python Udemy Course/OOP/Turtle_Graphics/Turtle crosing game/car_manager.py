from turtle import Turtle
import random
import time

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.SPAWN_CHANCE = 3
    
    def new_cars(self):
        if random.randint(1, self.SPAWN_CHANCE) == 1:
            new_turtle = Turtle("square")
            new_turtle.penup()
            new_turtle.shape("square")
            new_turtle.color(random.choice(COLORS))
            new_turtle.turtlesize(stretch_wid = 1, stretch_len = 3)
            new_turtle.goto(random.randint(250, 280), random.randint(-250,250))
            self.cars.append(new_turtle)
        
    def car_move(self):
        for car in self.cars:
            car.backward(self.car_speed)
    
    def increas_Speed(self):
        self.car_speed += MOVE_INCREMENT 
            

