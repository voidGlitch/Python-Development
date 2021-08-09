# with open("E:\\python on udemy\\Day25\\weather_data.csv") as file :
#   all_file=file.readlines()

# for names in all_file:
#   print(names)
 




# import csv

# with open("E:\\python on udemy\\Day25\\weather_data.csv") as data_file:
#   data = csv.reader(data_file)
#   temperature =[]
#   for row in data:
#     # print(row)
#     # print(row[1])
#     if row[1] == 'temp':
#       pass
#     else:
#       new_var = int(row[1])
#       temperature.append(new_var)
#       print(new_var)

#   print(temperature)

import pandas
data = pandas.read_csv("E:\\python on udemy\\Day25\\weather_data.csv")
print(data)

print(data["temp"])