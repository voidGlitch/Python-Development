height = int(input("please enter your height in centimeter \n"))
bill=0
age = int(input("please enter your age \n"))
if(height>=120):
    print("you can have a rollar coster ride")
    if(age<12):
        print("your ticket price is $7")
        bill=7
    elif(age<18):
        print("your ticket price is $10")
        bill=10
    else:
        print("your ticket price is $15")
        bill=15
    answer=input("do you want any photos press y / n")
    if(answer == "y"):
        bill=bill+5
        print("you are charged $5 extra ")
        print(f"you total price is ${bill}")
    if(answer == "n"):
        print("ok")
        print(f"you total price is ${bill}")

else:
    print("sorry you cant ride now")