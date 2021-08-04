from turtle import Turtle,Screen, xcor
import time


screen =Screen()
screen.bgcolor("black")
screen.setup(width=600,height=600)
screen.title("snake Game")
screen.tracer(0)  # in screen tracer If n is 0 (zero), automatic screen updates are off.
#  you need to explicitly call update() when you want the screen to reflect the current state of the drawing.

starting_postion = [ (0,0),(-20,0),(-40,0) ]
segments =[]

for positions in starting_postion:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(positions) 
    segments.append(new_segment)

game_is_on = True
while game_is_on:
    screen.update() # call update() when you want the screen to reflect the current state of the drawing.
    time.sleep(1)  #delay the time for 1 sec and then resets the screen
    # for seg in segments:
    #     seg.forward(20)
        #  screen.update() ❌not used because it updates the screen peice by peice but we want the whole bloack to be moving    


    for seg_num in range (len(segments)-1,0,-1):   #range() takes no keyword arguments
        new_x = segments[seg_num-1].xcor()   # takes cordinates from  the next segment because we are dealing in reverse order
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)   # set the cordinate of previous segment to the next segment
    segments[0].forward(20)
    
    segments[0].right(90)
    







        

screen.exitonclick()