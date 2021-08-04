import turtle as t
import random
tim=t.Turtle()

t.colormode(255)
direction =[0,90.180,360]
tim.width(10)



def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    colour =(r,g,b)
    return colour


for n  in range(200):
    colour = random_color()
    tim.color(colour)
    tim.forward(30)
    tim.setheading(random.choice(direction))