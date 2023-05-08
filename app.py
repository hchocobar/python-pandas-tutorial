import pandas as pd
# data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
# print(data_frame)

# 4.0
# ages = [23,45,7,34,6,63,36,78,54,34]
# data = pd.Series(ages)
# print(data)

# 4.1
# date_time_index = pd.date_range('05-01-2021', '05-12-2021')
# print(date_time_index)

# 4.2
# my_series = pd.Series([2, 4, 6, 8, 10])
# print(my_series.apply(lambda x: x / 2))

# 5
"""
data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
df = pd.DataFrame(data, columns=['Brand', 'Model', 'Color'])
print(df)
"""

# 5.1 
"""
data = [
    { 
        "brand": "Toyota", 
        "make": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "make": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porche", 
        "make": "Cayenne",
        "color": "White"
    },
        {
        "brand": "Tesla", 
        "make": "Model S",
        "color": "Red"
    }

]
df = pd.DataFrame(data)
print(df)
"""

# 5.2
"""
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.iloc[133, 6])
"""

# 5.3
"""
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.head(3))
"""

# 5.4
"""
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.tail(3))
"""

# 5.5
"""
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame[['Name', 'Type 1']][0:10])
"""

# 5.6
"""
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame.loc[data_frame['Attack'] > 80])
"""

# 5.7
"""
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(len(data_frame.loc[data_frame['Legendary'] == True]))
"""

# 6
"""
data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
print(data_frame.head())
"""

# 6.1
"""
data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
del data_frame[data_frame.columns[0]]
print(data_frame.head())
"""

# 6.3
"""
data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
print(data_frame.value_counts('Gender'))
# count = data_frame['Gender'].value_counts()
# count = data_frame.value_counts('Gender')
# print(count)
"""

# 6.2

data_frame = pd.read_csv('.learn/assets/us_baby_names_right.csv')
df = data_frame.groupby(['Name'])
print(len(df.sum()))