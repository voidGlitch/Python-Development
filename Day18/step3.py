from turtle import Turtle,Screen, color
from random import choice
color = ["red","blue","green","pink","green","black","purple","orange","lime","yellow"]
tim = Turtle()
i=0
def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for t in range(no_of_sides):
        tim.forward(100)
        tim.right(angle)

for sides in range(3,11):
    tim.color(choice(color))
    draw_shape(sides)

screen =  Screen()
screen.exitonclick()