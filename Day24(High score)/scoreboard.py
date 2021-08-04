from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

with open("E:\\python on udemy\\Day24(High score)\\data.txt",mode="r") as file:
    content = file.read()

HIGH_SCORE = int(content)
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score= HIGH_SCORE
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("E:\\python on udemy\\Day24(High score)\\data.txt",mode="w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


