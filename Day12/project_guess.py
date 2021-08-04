import random

def hard(random_number,attempt):
    while attempt!=0:
        
        user_input = int(input("please guess any input you think "))
        if(user_input==random_number):
            print("CONGRATULATION ! you have find the correct number🥳")
            return
        elif(random_number>user_input):
            print("please take another input with larger number😄")
            attempt=attempt-1
            print(f"you have only {attempt} attempts")
        elif(random_number<user_input):
            print("please choose a smaller number🧐")
            attempt=attempt-1
            print(f"you have only {attempt} attempts")
    if attempt == 0:
        print("you have used you attempts to maximum🙄.Please try agin later🤐")
        print(f"actual number was {random_number}")
def easy(random_number,attempt):
    while attempt!=0:
        
        user_input = int(input("please guess any input you think "))
        if(user_input==random_number):
            print("CONGRATULATION ! you have find the correct number🥳")
            return
        elif(random_number>user_input):
            print("please take another input with larger number😄")
            attempt=attempt-1
            print(f"you have only {attempt} attempts")
        elif(random_number<user_input):
            print("please choose a smaller number🧐")
            attempt=attempt-1
            print(f"you have only {attempt} attempts")
    if attempt == 0:
        print("you have used you attempts to maximum🙄.Please try agin later🤐")
        print(f"actual number was {random_number}")

print("welcome to the guess the number")
random_number=random.randint(0,100)
level = input("choose the level \n 1-hard level (only 5 attempts) \n 2-easy level(ony 10 attempts)\n ")
if(level=="hard" or level == "1"):
    attempt = 5
    print(f"You have choosen hard level you have only {attempt} attempts")
    hard(random_number,attempt)
elif(level=="easy" or level == "2"):
    attempt = 10
    print(f"You have choosen easy level you have only {attempt} attempts")
    easy(random_number,attempt)
