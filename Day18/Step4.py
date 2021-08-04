from turtle import Screen, Turtle,screensize
from random import choice
tim = Turtle()
color = ["red","blue","green","pink","green","black","purple","orange","lime","yellow"]
direction= [0,90,180,360]
def random_direction():
        tim.forward(50)
        tim.setheading(choice(direction))
        
for moves in range(300):
    tim.speed("fastest")
    tim.color(choice(color))
    tim.width(10)
    random_direction()








screen =Screen()
screen.screensize(200,1500)
screen.exitonclick()
