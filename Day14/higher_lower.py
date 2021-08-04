from hashlib import scrypt
from mmap import ACCESS_COPY
from art import logo 
from game_data import data
import random

print(logo)
score = 0
to_be_continued = True
account_b = random.choice(data)
while to_be_continued:
# genertaing two acoounts
    account_a = account_b
    account_b = random.choice(data)
    # if by chance both account becomes same
    while(account_a == account_b):
        account_b = random.choice(data)

    # A account details
    account_name_a= account_a['name']
    account_description= account_a['description']
    account_country= account_a['country']
    account_followers_a=account_a['follower_count']
    print(f"{account_name_a} , {account_description}  , {account_country}")

    # B account details
    account_name_b= account_b['name']
    account_description= account_b['description']
    account_country= account_b['country']
    account_followers_b=account_b['follower_count']
    print(f"{account_name_b} , {account_description} , {account_country}")


    # comparing there followers

    def compare_followers(follower_a,follower_b):
        if (follower_a>follower_b):
            print(f"followers of {account_name_a} has more .{follower_a}")
        else:
            print(f"followers of {account_name_b} has more followers .{follower_b}")


    # comparing guess with actual answer
    def compare_guess(guess,follower_a,follower_b):
        if(guess == f"{account_name_a}" or guess == "A" and follower_a>follower_b):
            return True
        elif(guess == f"{account_name_a}"or guess == "A" and follower_a<follower_b):
            return False
        elif(guess == f"{account_name_b}" or guess == "B" and follower_a>follower_b):
            return False
        elif(guess == f"{account_name_b}" or guess == "B" and follower_a<follower_b):
            return True

    # taking input from the user who has more followers
    user_guess = input(f"who do you thing has more followers\n 1.{account_name_a} \n 2. {account_name_b} \n")
    guess = user_guess.title()

    if(guess == f"{account_name_a}" or guess == "A"):
        print(f"you have choosen {account_name_a}")

    if(guess == f"{account_name_b}" or guess == "B"):
        print(f"you have choosen {account_name_b}")

    
    compare_followers(follower_a=account_followers_a,follower_b=account_followers_b)
    is_correct = compare_guess(guess,account_followers_a,account_followers_b)
    if is_correct == True:
        score = score +1
        print(f"you are correct.Your current score is {score}")
    else:
        print("Sorry!! you are wrong .Game over")
        to_be_continued = False
print(f"your final score is {score}")
