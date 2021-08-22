import pandas
data = pandas.read_csv("E:\\python on udemy\\Day25\\2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# returns all the coloumn which contain gray
# squirell_count= data[data.PrimaryFurColor == "Gray"]
# print(squirell_count)
gray_squirell_count= len(data[data.PrimaryFurColor == "Gray"])
print(gray_squirell_count)
black_squirell_count= len(data[data.PrimaryFurColor == "Black"])
print(black_squirell_count)
Cinnamon_squirell_count= len(data[data.PrimaryFurColor == "Cinnamon"])
print(Cinnamon_squirell_count)

data_dict ={
 "fur colour" :["Gray","Cinnamon","Black"],
 "count":[gray_squirell_count,black_squirell_count,Cinnamon_squirell_count]
}
print(data_dict)

dt= pandas.DataFrame(data_dict)
dt.to_csv("E:\\python on udemy\\Day25\\data_squirrel.csv")