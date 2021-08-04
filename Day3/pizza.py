size = input ("please enter what size of pizza do you want ? s, m , l \n")
bill=0
if( size == "s"):
    bill= 15
    print("you small size pizza is ready")
    add= input ("do you want to add pepper? y or n \n")
    if(add == "y"):
        bill=bill+2
        print("pepper added")
elif( size == "m"):
    bill= 20
    print("you medium size pizza is ready")
    add= input ("do you want to add pepper? y or n \n")
    if(add == "y"):
        bill=bill+3
        print("pepper added")
elif( size == "l"):
    bill= 25
    print("you large size pizza is ready")
    add= input ("do you want to add pepper? y or n \n")
    if(add == "y"):
        bill=bill+3
        print("pepper added")
else:
    print("invalid input")
cheese= input ("do you want to add extra cheese? y or n \n")
if(cheese == "y"):
        print("youare charged extra $1")
        bill =bill+1
else:
    print("ok")
print(f"you have orderd {size} pizza with {add} pepper and {cheese} cheese  Your total bill is ${bill} ")
