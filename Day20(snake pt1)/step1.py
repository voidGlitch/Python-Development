from turtle import Turtle,Screen

# tim = Turtle()
# tim.shape("square")
# tim.color("white")

# tim.stamp()
# tim.backward(20)
# tim.stamp()
# tim.backward(20)

#or

starting_postion = [ (0,0),(-20,0),(-40,0) ]

for positions in starting_postion:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.goto(positions)

screen =Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("snake Game")
screen.exitonclick()