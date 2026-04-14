import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data.csv")

# Calculate total and average using NumPy
df["total"] = np.sum(df[["math", "science", "english"]], axis=1)
df["average"] = np.mean(df[["math", "science", "english"]], axis=1)

# Find top student
top_student = df.loc[df["total"].idxmax()]

# Subject-wise average
subject_avg = df[["math", "science", "english"]].mean()

# Print results
print("Top Student:")
print(top_student[["name", "total"]])

print("\nSubject Averages:")
print(subject_avg)

# Plot graph
subject_avg.plot(kind="bar")
plt.title("Average Marks per Subject")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()