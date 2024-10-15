import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
scoreboard = Scoreboard()
cars = []
screen.listen()
screen.onkey(turtle.move, 'Up')

game_is_on = True
itetation = 0
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if itetation % 6 == 0:
        car = CarManager(scoreboard.score)
        cars.append(car)
    for car in cars:
        car.move()
        if turtle.distance(car) < 25:
            game_is_on = False
            scoreboard.game_over()
    itetation += 1

    #When turtle reach opposite side
    if turtle.ycor() > 280:
        turtle.update_position()
        scoreboard.increase_score()

        for car in cars:
            car.update_speed()

screen.exitonclick()

