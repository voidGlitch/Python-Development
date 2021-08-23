import random
names = ["alex","mike","harry","sid","jake","angela"]
# new_dict = {new_key:new_value for items in list}
student_score = {students:random.randint(30,100) for students in names}
print(student_score)

passed_students = {students:value for (students,value) in student_score.items() if value>60}
print(passed_students)