from turtle import Turtle,Screen, color
import random



screen = Screen()
screen.setup(width=500,height=500)

colours = ["blue","green","red","yellow","pink","grey","black"]
y_position = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    tim = Turtle(shape="turtle")
    tim.color(colours[turtle_index])
    tim.penup()
    tim.goto(x=-230,y=y_position[turtle_index])

#or you can do this

# pin= Turtle(shape="turtle")
# pin.color(colours[1])
# pin.penup()
# pin.goto(x=-230,y=-70)

# gim = Turtle(shape="turtle")
# gim.color(colours[2])
# gim.penup()
# gim.goto(x=-230,y=-40)

# lim = Turtle(shape="turtle")
# lim.color(colours[3])
# lim.penup()
# lim.goto(x=-230,y=-10)

# kim = Turtle(shape="turtle")
# kim.color(colours[4])
# kim.penup()
# kim.goto(x=-230,y=20)

# nim = Turtle(shape="turtle")
# nim.color(colours[5])
# nim.penup()
# nim.goto(x=-230,y=50)

# Fim = Turtle(shape="turtle")
# Fim.color(colours[6])
# Fim.penup()
# Fim.goto(x=-230,y=80)




screen.exitonclick()