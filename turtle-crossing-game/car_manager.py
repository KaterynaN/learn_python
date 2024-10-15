from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self, reach_goal):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.update_position()
        self.reach_goal = reach_goal
        self.car_speed = STARTING_MOVE_DISTANCE + reach_goal * MOVE_INCREMENT

    def update_position(self):
        self.setheading(180)
        self.goto(280, random.randint(-250, 250))

    def move(self):
        self.forward(self.car_speed)

    def update_speed(self):
        self.car_speed += MOVE_INCREMENT
