def prime_checker(number):
    is_prime= True
    for n in range(2,number):
        if(number%n==0):
            is_prime = False
    if is_prime == True:
        print("it is a prime number")
    else:
        print('its not a prime number')
count=1
while(count):
    n = int(input("please enter your number\n"))
    prime_checker(number=n)
    count = int(input("continue? press 1 or 0\n"))