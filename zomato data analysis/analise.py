import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import os

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    
clear_terminal()

dataframe = pd.read_csv("Zomato data .csv")
print(dataframe.head())

def handleRate(value):
    value = str(value).split('/')
    value = value[0]
    return float(value)

dataframe['rate'] = dataframe['rate'].apply(handleRate)
print(dataframe)

#dataframe.info()

sns.countplot(x = dataframe["listed_in(type)"])
plt.xlabel("type of reaturants")
plt.show()

grouped_data = dataframe.groupby('listed_in(type)')['votes'].sum()
result = pd.DataFrame({'votes' : grouped_data})
plt.plot(result,c= "green" , marker = "o")
plt.xlabel("votes", c = "red" , size = 20)
plt.ylabel("type of restaurent",c = "red", size = 20)
plt.show()

dataframe.head()

plt.hist(dataframe['rate'],bins = 5 )
plt.title("rating distribution")
plt.show()

couple_data=dataframe['approx_cost(for two people)']
sns.countplot(x = couple_data)
plt.show()

plt.figure(figsize = (6,6))
sns.boxplot(x= 'online_order', y ='rate', data = dataframe)
plt.show()


pivot_table = dataframe.pivot_table(index='listed_in(type)', columns='online_order')
print(pivot_table.dtypes)
sns.heatmap(pivot_table, annot=True, cmap="YlGnBu", fmt='d')
plt.title("Heatmap")
plt.xlabel("online order")
plt.ylabel("listed in (type)")
plt.show()
