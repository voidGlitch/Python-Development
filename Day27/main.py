import tkinter

window = tkinter.Tk()
window.title("GUI Program")
window.minsize(width=500,height=300)

#Label

# create a component
mylabel = tkinter.Label(text="I am a label",font=("Arial",24,"italic"))
# component call
# geometery management system attributes : side,expand
mylabel.pack(expand=True)
# Adv py arguments
'''
1) keyword arguments
2) arguments with def values
'''







#while true condition loop
window.mainloop()
