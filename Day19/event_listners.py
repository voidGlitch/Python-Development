from turtle import Turtle,Screen

tim = Turtle()

def move_forward():
    tim.forward(20)

screen = Screen()
screen.listen()
# higher order function
# rember if we add function inside a function it will not include paranthesis i.e ""
screen.onkey(key="space",fun = move_forward)
screen.exitonclick()