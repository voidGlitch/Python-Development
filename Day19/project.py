from turtle import Turtle,Screen, color
import random
import turtle


is_stop =False
screen = Screen()
screen.setup(width=500,height=500)
user_bet = screen.textinput(title="please choose a bet",prompt="what is you guess")

colours = ["blue","green","red","yellow","pink","grey","black"]
all_turtle =[]

y_position = [-70,-40,-10,20,50,80]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])   # we have to sub 20 because the turtle is 20m long
    all_turtle.append(new_turtle)

if user_bet:
    is_stop=True

while is_stop:



    for turtles in all_turtle:

        if turtles.xcor() > 220:  #same as above we have to subtract 30 to get the end of the part
            is_stop =False
            winning_color = turtles.pencolor()
            if winning_color == user_bet:
                print(f"congratulation! you have win the {winning_color} turtle")
            else:
                print(f"sorry! you lost from the {winning_color} turtle")
        rand_distance = random.randint(0,10)
        turtles.forward(rand_distance)




screen.exitonclick()