import random

names_string = input("please enter the names seperated by ',' in between \n")
names = names_string.split(",")
# print(names)
print(f"{names} among them")
length = len(names) - 1
random_name = random.randint(0,length)
print(f"{names[random_name]} is going to buy the meal today")