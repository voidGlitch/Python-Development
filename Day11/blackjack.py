import random
from art import logo
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_card= random.choice(cards)
    return user_card

def calculator_score(cards):
    '''takes a list oof cards from the user or computer and calculate the sum of cards'''
    # if 11 in cards and 10 in cards and len(cards) == 2: or
    if sum(cards) == 21 and len(cards)==2:
        return 0 

    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)


    return sum(cards)
    # for numbers in player_card:
    #     num1 = num1 + numbers
    # print(num1)
    # for numbers in computer_card:
    #     num2= num2 +numbers
    # print(num2)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return "its a draw 😁"
    elif user_score==0:
        return "you win🤩.you have blackjack"
    elif computer_score==0:
        return "you lose😓.computer have blackjack"
    elif computer_score>21:
        return "computer went over you win😂."
    elif user_score>21:
        return "you went over computer win😣"
    elif computer_score>user_score:
        return "you lose😭"
    else:
        return "you win😄"



def playgame():
    print(logo)
    user_card = []   
    computer_card = []   
    is_game_over = False
    for _ in range(0,2):
        new_card = deal_card()
        user_card.append(new_card)

    for _ in range(0,2):
        new_card = deal_card()
        computer_card.append(new_card)
    while not is_game_over:
        user_score = calculator_score(user_card)
        computer_score = calculator_score(computer_card)
        print(f"your cards are {user_card} and your total score is {user_score}")
        print(f"computer card is {computer_card[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over= True
        else:
            user_should_deal = input("type 'y'to get another card else type'n' to pass : ")
            if user_should_deal == "y":
                user_card.append(deal_card())
            else:
                is_game_over = True

    while computer_score == 0 and computer_score>17:
        computer_card.append(deal_card())
        computer_score = calculator_score(computer_card)

    
    print(f"your final cards were{user_card} and final score was {user_score} ")
    print(f"computer final cards were{computer_card} and final score was {computer_score} ")
    print(compare(user_score,computer_score))
should_continue=True
while should_continue:
        if input("do you wnt to play the game blackjack? 'y' or 'n' :") == "y":
            playgame()
            
        else:
            print("thanks for coming")
            should_continue=False