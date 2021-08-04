students = input("please ente the height of the students \n").split()

for n in range(0,len(students)):
    
    students[n]=int(students[n])
    
# for n in students:
#     print(n)
#     n[len(students)] = int(n[len(students)])
print(students)
total_height = 0
for heights in students:
    total_height = total_height + heights
print(total_height)
total =0
for student in students:
    total= total +1
print(total)
average = round(total_height / total)
print(f"your average height is {average}")