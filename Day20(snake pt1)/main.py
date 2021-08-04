from turtle import Turtle,Screen, xcor
import time
from snake import Snake


screen =Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("snake Game")
screen.tracer(0) 


snake = Snake()

screen.listen()
screen.onkey(snake.up , "Up")
screen.onkey(snake.down , "Down")
screen.onkey(snake.left , "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update() 
    time.sleep(0.1)  # delay the time for 1 sec and then resets the screen
    
    
    snake.move()
    
screen.exitonclick()