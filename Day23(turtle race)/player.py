from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)    
        self.color("red")
        self.setheading(90)
        self.shapesize(stretch_wid=1,stretch_len=1)

    def move_turtle(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)
        
    def side_left(self):
        new_x = self.xcor() - MOVE_DISTANCE
        self.goto(new_x,self.ycor())

    def side_right(self):
        new_x = self.xcor() + MOVE_DISTANCE
        self.goto(new_x,self.ycor())

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def refresh_position(self):
        self.goto(STARTING_POSITION)