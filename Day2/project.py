bill = float(input("please enter the amount of the bill \n"))
tip = int(input("please neter the amout of tip you want to give.Let's say 10 , 20 or 30 \n"))
percent = bill * (tip / 100)
percent = round(percent,2)
print(percent)
total = bill + percent
total = round(total,2)
print(total)
share = int(input("among how many people youwnt to split the bill \n"))
per =  total / share
per = round(per ,2)
print(f"your total price is {total} which is sahred among {share} peoples and hence the total cost per share is {per}")