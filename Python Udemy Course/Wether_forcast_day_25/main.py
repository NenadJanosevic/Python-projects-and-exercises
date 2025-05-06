# with open("weather_data.csv" ,"r") as data:
#     print(data.readlines())

# import csv

# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperature = []
#     for row in data:
#         if row[1].isdigit():
#             row[1]= int(row[1])
#             temperature.append(row[(1)])
#     print(temperature)
    
# import pandas


# data = pandas.read_csv('weather_data.csv')
# print(data["temp"])

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# x = 0 
# temp_list = data["temp"].to_list()
# for num in temp_list:
#     x += num
# print(x / len(temp_list))

# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# temp_list = data["temp"].to_list()
# print(data["temp"].max())

# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
import pandas as pd

grey = []
red = []
black = []

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey_squirrel = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrel)
for color in data["Primary Fur Color"]:
    if pd.notna(color):
        if color == "Gray":
            grey.append(color)
        elif color == "Cinnamon":
            red.append("Cinnamon")
        else:
            black.append("Black")

squirrel_count ={
    "Fur color":["grey", "red", "black"],
    "count":[len(grey), len(red), len(black)]
}
df = pd.DataFrame(squirrel_count)
df.to_csv("squirrel_count.csv", index = False)
