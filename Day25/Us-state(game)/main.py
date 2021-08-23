from os import stat_result
import turtle
import pandas
screen = turtle.Screen()
image = 'Day25\\Us-state(game)\\blank_states_img.gif'
screen.addshape(image)

turtle.shape(image)

# to get the location of states on screen 

# def get_mouse_click(x,y):
#  print(x,y)

# turtle.onscreenclick(get_mouse_click)

# screen.mainloop()

def goto_loc(x,y,input):
 t = turtle.Turtle()
 t.hideturtle()
 t.penup()
 t.goto(x,y)
 t.write(f"{input}",align = "center" , font= ("Courier",8,"normal")) 


data = pandas.read_csv("E:\\python on udemy\\Day25\\Us-state(game)\\50_states.csv")
all_states =data.state.to_list()
guessed_state =[]
while len(guessed_state) < 50:
 if len(guessed_state) == 0:
  user_input = turtle.textinput(title="Guess the states",prompt="What is your choice")
 else:
  user_input = turtle.textinput(title=f"{len(guessed_state)}/{len(data)} here input",prompt="What is your choice")
 input = user_input.capitalize()


 if input == "Exit":
  missed_state = [states for states in all_states if states not in guessed_state]
  # for states in all_states:
  #  if states not in guessed_state:
  #   missed_state.append(states)
  dt = pandas.DataFrame(missed_state)
  dt.to_csv("E:\\python on udemy\\Day25\\Us-state(game)\\missed_states.csv")
  break
 if  input in all_states:
  guessed_state.append(input)
  location = data[data.state == input]
  x_cor = int(location.x)
  y_cor = int(location.y)
  # print(data.state.item())  error
  goto_loc(x_cor,y_cor,input)
  #or
  # goto_loc(x_cor,y_cor,data.state.item()) error


#outside the while loop

print(missed_state)

