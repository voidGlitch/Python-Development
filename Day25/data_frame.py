import pandas
data = pandas.read_csv("E:\\python on udemy\\Day25\\weather_data.csv")
print(type(data)) # dataframe

print(type(data["temp"]))  #series It is kind of like a single column list
#there are two type of primary data structure
