import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import pyplot

# Replace the URL with the local file path or correct URL pointing directly to a CSV file
file_path = r"C:\Users\SARVESH\Desktop\Anime_rank.csv"

headers = ["UID","title", "rank", "Streamtype", "Episodes", "Start date","End date ", "members","Score"]

# Reading the CSV file
df = pd.read_csv(file_path, header= None, names=headers)
#Removing headers=none will have no effect
#Displaying the first few rows of the dataframe
print(df)
#print df prints entire dataset and df.tail prints from below
print(df.dtypes)
#gives the datatypes of datas
df["members"] = df["members"].str.replace(',','').astype("Int64")
#changes the members column from string(object) to float


print(df.describe())
#gives the stastical data of numerical columns in the form of count , mean , std ,min ,25% ,50%,75%,max 
print(df.columns)
#lists the columns of dataset

#path = 'path of file '
#df.to_csv - saves the file in csv format 

print(df.describe(include='all'))

bin = np.linspace(min(df["Episodes"]),max(df["Episodes"]), 3)
#generates array for bin i.e bin edges 3-1=2 edges

groups = ["Less","more"]
#name of the edges

df["Episodes-binned"] = pd.cut(df["Episodes"], bin , labels=groups , include_lowest= True)
#cuts the data into bins and labels them
episode_counts = df["Episodes-binned"].value_counts().sort_index()
pyplot.bar(episode_counts.index, episode_counts.values)
pyplot.xlabel("Episodes")
pyplot.ylabel("Count")
pyplot.title("Episodes Binned")
pyplot.show()
#creates histogram of bins 


streamtype_dummies = pd.get_dummies(df['Streamtype'], prefix='Streamtype')
#creates dummy variables for the streamtype column
df = pd.concat([df, streamtype_dummies], axis=1)
#Assigns value true/false to dummies

#The below code block prints a scatterplot of episodes vs members
print(df)

y=df["Episodes"]
x=df["members"]

plt.scatter(x,y)

plt.title("Episodes vs members")
plt.xlabel("Members")
plt.ylabel("episodes")
plt.show()
#creates scatterplot of episodes vs members
df_test = pd.DataFrame( columns=['Streamtype','Start date','End date','Score'])
   
df_grp = df_test.groupby(['Streamtype','Start date','End date'], as_index=False).mean()
print(df_grp)
