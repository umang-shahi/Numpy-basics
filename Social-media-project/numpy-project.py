import pandas as pd
import numpy as np

df = pd.read_csv("data.csv")

print(df.head())

avg_age = np.mean(df["age"])
print("Average Age:", avg_age)

print("Max Age:", np.max(df["age"]))
print("Min Age:", np.min(df["age"]))

total_addiction = np.sum(df["addiction_level"])
print("Total Addiction Score:", total_addiction)

std = np.std(df["addiction_level"])
print("Std Dev:", std)

age_array = df["age"].values
print(age_array)

high_addiction = df[np.array(df["addiction_level"]) > 5]
print(high_addiction.head())

