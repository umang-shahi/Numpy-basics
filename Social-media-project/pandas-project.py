import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

duplicates = df.drop_duplicates()    #remove duplicate rows

missing_values = df.dropna()         #remove missing values

df["age"]  = df["age"].astype(int)    #fix data types



high_addiction = df[df["addiction_level"] > 5]      #filtering data


young_users = df[(df["age"] < 25) & (df["addiction_level"] > 7)]
#print(young_users, "users of young age:")


grouped = df.groupby("gender")['addiction_level'].mean()
#print(grouped)



summary = df.agg({
    "age" : ["mean", "max","sum"],
    "addiction_level" : ["mean", "sum"]
})

#print(summary)


#print(df.duplicated())


df["risk_level"] = np.where(df["addiction_level"] > 7, "High", "Low")

print(df.head())

#top_users = df.sort_values(by="addiction_level", ascending=false).head(5)

##combining two data sets

#df2 = pd.read_csv("users.csv")

#merged = pd.merge(df, df2, on="user_id", how="inner")


#print(df["gender"].value_counts())




