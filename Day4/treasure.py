row1 = [ "😶" , "😶" , "😶"]
row2 = [ "😶" , "😶" , "😶"]
row3 = [ "😶" , "😶" , "😶"]
treasure =[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}\n")
point =input("enter the loction where you want to hide the treasure \n")

horizontal = int(point[0])
vertical =int(point[1])

row= treasure[ horizontal- 1 ]
row[ vertical-1 ]="X"
# row[treasure[vertical]]


print(f"{row1}\n{row2}\n{row3}\n")