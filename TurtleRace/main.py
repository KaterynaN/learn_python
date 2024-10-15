from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
user_bet = screen.textinput(title="Place your bet", prompt="Which turtle will win the race? Place the color")
x = -230
y = -180
all_turtles = []
for color in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(color)
    turtle.penup()
    y += 50
    turtle.goto(x, y)
    all_turtles.append(turtle)


if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"The {winning_color} turtle was first. You've won!")
            else:
                print(f"The {winning_color} turtle was first. You've lost!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
print(user_bet)
