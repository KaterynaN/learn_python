import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
dict = data['Primary Fur Color'].value_counts()
count_colors = dict.to_dict()
data_dict = {}
colors = []
count = []
for key, value in count_colors.items():
    colors.append(key)
    count.append(value)

data_dict['Color'] = colors
data_dict['Count'] = count
print(data_dict)

data = pandas.DataFrame(data_dict)
data.to_csv("squirrel_count_by_color.csv")
