from turtle import Turtle, Screen
SNAKE_SIZE = 3
MOVE_DISTANCE = 20
SEGMENT_SIZE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]


    def create_snake(self):
        x = SEGMENT_SIZE
        for _ in range(SNAKE_SIZE):
            self.add_segment((x, 0))
            x -= SEGMENT_SIZE

    def add_segment(self, position):
        piece = Turtle(shape="square")
        piece.color("white")
        piece.penup()
        piece.goto(position)
        self.snake_body.append(piece)

    def reset(self):
        for seg in self.snake_body:
            seg.goto(1000, 1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for segment in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[segment - 1].xcor()
            new_y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(new_x, new_y)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)



