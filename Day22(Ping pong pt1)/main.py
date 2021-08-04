from turtle import Turtle,Screen
from ball import Ball
import time
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)



r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))

ball = Ball()
score= ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.refresh()
#detect the collision with wall
    if ball.ycor() >270 or ball.ycor() < -270:   #i.e 280>270 or -290 < -270
        #bouncer back the ball when hits the collision
        ball.bounce_y()
#detect colission with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
#detect whren the ball collide with the wall on r _side
    if ball.xcor() >380:
        ball.game_over()
        score.l_point()
        
        
#detect whren the ball collide with the wall on l_side
    if ball.xcor() <-380:
        ball.game_over()
        score.r_point()

screen.exitonclick()