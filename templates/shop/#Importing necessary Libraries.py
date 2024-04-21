#Importing necessary Libraries
import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

#Reading the data from csv file

#setting up pandas
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.max_colwidth', 18)
pd.set_option('display.max.columns',8) 
df=pd.read_csv("C:\\Users\\ADMIN\\Downloads\\Restaurant-Reviews.csv" )
#print(df.head(5))

#Data cleaning
df.drop(columns=['7514','Review'], inplace=True)#getting rid of 7514 column since it contains only one value

df.duplicated().sum() # checking for duplicates, we have 36 duplicates in our dataset which needs to be removed
df.drop_duplicates(inplace=True)
df.isnull().sum() #checking and dropping null values
df.dropna(inplace=True)
df["Rating"].value_counts() #checking unique values under rating column
df["Rating"].replace({"Like":4})
df['Rating']=df["Rating"].replace({"Like":"4"}) #Replacing 'like' rating with 4
df["Rating"]=df["Rating"].astype(float)
df["Time"]=pd.to_datetime(df["Time"]) #Converting Time into date time format
#Extracting data from Time column
df["Day"]=df["Time"].dt.day
df["Month"]=df["Time"].dt.month
df["Year"]=df["Time"].dt.year
df["Hour"]=df["Time"].dt.hour

#looping through hour column to categorize them into morning,afternoon, evening and ninght then create a column 
print(df)
# time_of_day.py
def time_of_the_day(hour):
    if hour >= 1 and hour <= 4:
        return "Early Morning"
    elif hour >= 5 and hour <= 12:
        return "Morning"
    elif hour >= 13 and hour <= 15:
        return "Afternoon"
    elif hour >= 16 and hour <= 21:
        return "Evening"
    else:
        return "Late Night"