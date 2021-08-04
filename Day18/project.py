import turtle
from main import color_list
from turtle import Turtle,Screen
import random
tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for _ in range(5):
    for _ in range(0,10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
        tim.dot(20,random.choice(color_list))
    tim.left(90)
    tim.forward(50)
    tim.setheading(180)
    for _ in range(10):
        tim.dot(20,random.choice(color_list))
        tim.forward(50)
        tim.dot(20,random.choice(color_list))
    tim.right(90)
    tim.forward(50)
    tim.setheading(360)









screen = Screen()
screen.exitonclick()