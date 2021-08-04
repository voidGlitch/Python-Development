user = input("you're at the cross road . Where do you wnt to go ?Type 'left' or'right' : \n")
if(user == "left"):
    user2 = input("you came to a lake. There is an island in hte middle of the lake . Type 'wait' to wait for the boat.Type 'swim' to swim across : \n ")
    if(user2 == "wait"):
        user3 = input("you  arrived at the island unarmed. There is houses  with 3 doors. one red, one yellow and one blue. Which color do you you choose : \n")
        if(user3=="blue"):
            print("you have win the treasure")
        elif(user3=="red"):
            print("you have choosen the fire .Game over")
        elif(user3=="yellow"):
            print("you  have choosen doors of snake. Game over")
        else:
            print("you have entered invalid input")
    else:
        print("game over")
else:
    print("game over")