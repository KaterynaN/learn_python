import turtle
from turtle import Turtle, Screen
from random import randint, choice
import colorgram

tim = Turtle()
tim.shape("turtle")
turtle.colormode(255)


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r, g, b)
    return random_color


# square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)

# dashed-line
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

def different_shapes(number_of_max_sides):
    for n in range(3, number_of_max_sides):
        degree = int(360 / n)
        tim.pencolor(random_color()),
        for i in range(n):
            tim.forward(100)
            tim.right(degree)


def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed("fastest")
    for _ in range(300):
        tim.pencolor(random_color()),
        tim.forward(30)
        tim.setheading(choice(directions))


#spirograph
def draw_spirograph(size_of_gap):
    tim.speed("fastest")
    tim.hideturtle()
    for _ in range(int(360 / size_of_gap)):
        tim.pencolor(random_color())
        tim.circle(100)
        tim.left(size_of_gap)


#herst_dots
colors = colorgram.extract('download.jpg', 20)
# tim.pensize(30)
# tim.forward(50)

# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb = (r, g, b)
#     rgb_colors.append(rgb)
# print(rgb_colors)
my_colors = [(239, 244, 249), (236, 225, 83), (202, 5, 72), (198, 164, 10), (235, 51, 129), (206, 76, 11),
             (108, 179, 218), (219, 162, 103), (234, 225, 6), (30, 188, 108), (23, 106, 173), (13, 23, 64),
             (17, 28, 175), (213, 135, 176), (9, 185, 214), (205, 29, 142), (229, 168, 197)]

screen = Screen()
def draw_row(dot_size, dots_in_row, space):
    for n in range(dots_in_row):
        tim.pendown()
        color = choice(my_colors)
        tim.dot(dot_size, color)
        tim.penup()
        tim.forward(space)
def herst_dots(dot_size, rows, dots_in_row, space):
    size = (dot_size + space) * dots_in_row
    screen.setup(size, size)
    # screen.setworldcoordinates(0, 0, SIZE, SIZE)
    tim.hideturtle()
    tim.penup()
    x = (dot_size + 50 - size / 2)
    tim.goto(x, x)
    for n in range(rows):
        tim.penup()
        tim.goto(x, x + (n * space))
        tim.pendown()
        draw_row(dot_size, dots_in_row, space)


def move_forwards():
    tim.forward(30)

def move_backwards():
    tim.backward(30)

def turn_left():
    tim.setheading(tim.heading()+10)

def turn_right():
    tim.setheading(tim.heading() - 10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="space", fun=clear)
#different_shapes(11)
# random_walk()
# draw_spirograph(5)
# herst_dots(20, 5, 5, 50)

screen.exitonclick()
