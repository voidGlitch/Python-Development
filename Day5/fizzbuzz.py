for num in range(1,101):
   
    if(num % 3 == 0 and num %5 ==0):
        print("fizzBuzz")
    elif(num % 3 == 0 ):
        print("fizz")
    elif(num %5 ==0):
        print("fizz")
    else:
        print(num)