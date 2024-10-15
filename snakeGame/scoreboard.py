from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.extract_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def extract_high_score(self):
        with open("data.txt") as file:
            self.high_score = int(file.read())

    def white_high_score(self):
        with open("data.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.white_high_score()
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.write(f"Game over\n Your score: {self.score}", align= ALIGNMENT, font= FONT)
