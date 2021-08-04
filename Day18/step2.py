from turtle import Turtle,Screen

tim = Turtle()

for tur in range(0,50):
    tim.forward(2)
    tim.penup()
    tim.forward(2)
    tim.pendown()


screen= Screen()
screen.exitonclick()