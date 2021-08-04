# from replit import clear
from art import logo
print(logo)
bids ={}
conti=True

def find_highest_bid(bidding_records):
    highest_bid=0
    winner=""
    for bidder in bidding_records:
        bid_amount = bidding_records[bidder]
        if bid_amount>highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"the winner is {winner} and the highest bid is ${highest_bid}")

while(conti):
    
    name = input("please enter your name \n")
    price = int(input("please enter your price \n"))
    bids[name] = price
    to_continue =input("do you wnat to continue? type 'yes' or 'no' \n")
    if(to_continue == "yes"):
        conti = True
        # clear()
    elif(to_continue == "no"):
        conti= False
        find_highest_bid(bids)