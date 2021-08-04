import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
while(True):
    user_choice=int(input("please enter input 1. for rock 2. for paper 3. for scissors\n"))
    if(user_choice == 1):
        print(rock)
    if(user_choice == 2):
        print(paper)
    if(user_choice == 3):
        print(scissors)
    computer_choice=random.randint(1,3)
    com=['rock','paper','scissors']
    print(f"computer chooses {com[computer_choice-1]}")
    if(computer_choice == 1):
        print(rock)
    if(computer_choice == 2):
        print(paper)
    if(computer_choice== 3):
        print(scissors)

    if(user_choice == computer_choice):
        print("its a tie")
    elif(user_choice ==1 and computer_choice == 2):
        print("you lose")
    elif(user_choice ==2 and computer_choice ==3):
        print("you lose")
    elif(user_choice ==3 and computer_choice ==1):
        print("you lose")
    else:
        print("you win")