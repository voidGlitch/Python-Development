from turtle import Turtle,Screen

tim = Turtle()

def move_forward():
    tim.forward(20)

def move_backward():
    tim.backward(20)

def clockwise():
    tim.right(30)

def anti_clockwise():
    tim.left(30)

def reset():
    tim.reset()


screen = Screen()
screen.listen()

screen.onkey(key="w",fun = move_forward)
screen.onkey(key="s",fun = move_backward)
screen.onkey(key="a",fun = clockwise)
screen.onkey(key="d",fun = anti_clockwise)
screen.onkey(key="c",fun = reset)

screen.exitonclick()