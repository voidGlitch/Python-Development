you = input("Please eneter your name here : \n")
you = you.lower()
pat = input("Please eneter your partner name here : \n")
pat = pat.lower()
name = you + pat
print (name)
t= name.count("t")
r= name.count("r")
u= name.count("u")
e= name.count("e")

true = t+ r+ u+ e

l= name.count("l")
o= name.count("o")
v= name.count("v")
e= name.count("e")

love = l+o+v+e
score = str(true) + str(love)
print(score)
print(type(score))
score = int(score)
print(f"you total score is {score}")
if(score<10 or score>90):
    print(f"your score is {score} and you go together like coke and mentos")
elif(score<40 or score>50):
    print(f"your score is {score} and you are alright together")
else:
    print("your score is " + str(score))