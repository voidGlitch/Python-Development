# with open("E:\\python on udemy\\Day25\\weather_data.csv") as file :
#   all_file=file.readlines()

# for names in all_file:
#   print(names)
 
import csv

with open("E:\\python on udemy\\Day25\\weather_data.csv") as data_file:
 data = csv.reader(data_file)

 for all in data:
  print(all)