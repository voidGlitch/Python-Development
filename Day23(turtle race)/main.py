import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard




screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle = Player()
car = CarManager()
score = Scoreboard()
screen.listen()

screen.onkey(turtle.move_turtle,"Up")
screen.onkey(turtle.down,"Down")
screen.onkey(turtle.side_left,"Left")
screen.onkey(turtle.side_right,"Right")





game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.generate_car()
    car.move_car()
#detect collision with wall
    if turtle.ycor() > 280 :
        score.point()
        turtle.refresh_position()
        car.increment()
        # car.refresh()
        print(f"speed increased to: {car.move_increment}")
#detect the collision with car
    for cars in car.all_cars:
        if cars.distance(turtle)<20:    
            game_is_on = False
            #print the game over in middle
            score.game_over()

screen.exitonclick()         
    