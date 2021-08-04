students = input("please enter the scores of the students \n").split()

for n in range(0,len(students)):
    
    students[n]=int(students[n])
    
print(students)
# print(max(students)) simple way
max = 0
for scores in students:
    
    if(max<scores):
        max = scores
print(f"your maximum number is {max}")
min = max
for scores in students:
    if(min>scores):
        min = scores
print(f"your minumum score is {min}")