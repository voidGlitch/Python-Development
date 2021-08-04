from turtle import Turtle
FONT =("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        
        self.score= 0 
        self.penup()
        self.hideturtle()
        self.score_board()

    def score_board(self):
        self.clear()
        self.goto(-250,250)
        self.write(f"level:{self.score}",align = "Left" , font= FONT)

    def point(self):
        self.score += 1
        self.score_board()
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align = "Center" , font= FONT)
        