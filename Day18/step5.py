from turtle import Turtle,Screen, color, setheading
import random
import turtle 
tim= Turtle()
turtle.colormode(255)
tim.speed("fastest")

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colour = (r,g,b)
    return colour
def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        tim.color(random_color())
    # or else we can do
    # tim.left(i)
    # tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)
        tim.circle(100)
draw_spirograph(50)
screen = Screen()
screen.exitonclick()