import pandas
data = pandas.read_csv("E:\\python on udemy\\Day25\\weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)
# length = len(temp_list)
# sum = sum(temp_list)

# average = sum/ length
# print(average)

# # or you can do the pandas work here we can do it mean mode and merdian

# print(data["temp"].mean())
# print(data["temp"].max())
# # get the data in coloumn.
# '''does exactly the same but it is pascal case dependent'''
# print(data.condition)
# print(data["condition"])

# get data in row

# print(data[data.day == "Monday"])
# max_temp = data["temp"].max()
# print(data[data.temp == max_temp ])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# temp_mon = monday.temp
# farehneit = (temp_mon * 9/5) + 32
# print(farehneit)

# data_dict ={
#  "students":["amy","lisa","angela"],
#  "marks":[76,56,54]
# }

# data_panda =pandas.DataFrame(data_dict)
# print(data_panda)
# data_panda.to_csv("E:\\python on udemy\\Day25\\new_data.csv")