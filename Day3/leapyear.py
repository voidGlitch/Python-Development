year = int(input("please enter your year to check"))
leap = year / 4
print(leap)
if(year % 4 == 0):
    if(year % 100 == 0):
     if(year % 400 == 0):
        print("it is leap year")
    else:
        print("it is a leap year here shusd")
else:
    print("it is not a leap year")