student_dict = {"students" :["miku","vidita","bebo"],
"score":[56,76,98]}
#lopping through dictionaries
# for (key,value) in student_dict.items():
#  print(key)
#  print(value)


import pandas

student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)

#loop through a data frame
# for (key, value) in student_data_frame.items():
#  # print(key)
#  print(value)


# pandas has inbuilt loop called it iterrows it allows us to lopp through each of the rows rather than each of the coloumn

for (index,row ) in student_data_frame.iterrows():
 # print(row)
 # print(row.students)
 # print(row.score)
 if row.students == "miku":
  print(row.score)