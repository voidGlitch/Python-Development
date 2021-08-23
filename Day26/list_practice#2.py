data1 = open("E:\\python on udemy\\Day26\\file1.txt","r")
number1=data1.readlines()
data2 = open("E:\\python on udemy\\Day26\\file2.txt","r")
number2=data2.readlines()

result = [int(num) for num in number1 if num in number2]
print(result)
# with open("./Day26/file1.txt") as file1:
#     list1 = file1.readlines()
    
# with open("./Day26/file2.txt") as file2:
#     list2 = file2.readlines()
    
# result = [int(num) for num in list1 if num in list2]

# # Write your code above 👆
# print(result)
number = [1,1,2,3,5,8,13,21,34,55]
rest = [numb for numb in number if numb%2==0]
print(rest)