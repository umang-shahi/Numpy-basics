import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv")

print(df.head())

gender_counts = df["gender"].value_counts()

plt.pie(gender_counts, labels=gender_counts.index, autopct="%1.1f%%")
plt.title("Gender Distribution")
plt.show()




plt.hist(df["age"], bins=10, color = 'red')

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()


plt.scatter(df["age"], df["addiction_level"], marker = "*")

plt.title("Age vs Addiction Level")
plt.xlabel("Age")
plt.ylabel("Addiction Level")

plt.show()



avg_by_age = df.groupby("age")["addiction_level"].mean()

avg_by_age.plot(kind="line")

plt.title("Average Addiction Level by Age")
plt.xlabel("Age")
plt.ylabel("Addiction Level")

plt.show()