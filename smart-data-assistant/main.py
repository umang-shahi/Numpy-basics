import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load CSV WITHOUT headers
df = pd.read_csv("data.csv")

print(df.head())

# Assign column names (based on your dataset)
df.columns = [
    "age","gender","addiction_level","platform",
    "daily_usage_hours","sleep_hours","mental_health_score",
    "stress_level","risk_level","focus_score",
    "academic_score","social_score","depression_label"
]

# Clean text (fix low/medium/high → Low/Medium/High)
df["risk_level"] = df["risk_level"].str.capitalize()

# ---------------- FUNCTIONS ---------------- #

def summary():
    print("\n📊 DATA SUMMARY")
    print("Total Users:", len(df))
    print("Average Age:", round(df["age"].mean(), 2))
    print("Average Addiction Level:", round(df["addiction_level"].mean(), 2))
    print("High Risk Users:", len(df[df["risk_level"] == "High"]))


def platform_analysis():
    print("\n📱 Platform Usage:")
    print(df["platform"].value_counts())


def bar_graph():
    df.groupby("risk_level")["addiction_level"].mean().plot(kind="bar")
    plt.title("Average Addiction by Risk Level")
    plt.xlabel("Risk Level")
    plt.ylabel("Addiction Level")
    plt.show()


def histogram():
    plt.hist(df["age"], bins=10)
    plt.title("Age Distribution")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.show()


def scatter():
    plt.scatter(df["age"], df["addiction_level"])
    plt.title("Age vs Addiction Level")
    plt.xlabel("Age")
    plt.ylabel("Addiction Level")
    plt.show()


def line_graph():
    avg_by_age = df.groupby("age")["addiction_level"].mean().sort_index()
    plt.plot(avg_by_age.index, avg_by_age.values)
    plt.title("Addiction Trend by Age")
    plt.xlabel("Age")
    plt.ylabel("Addiction Level")
    plt.show()


def generate_email():
    avg_age = df["age"].mean()
    high_risk = len(df[df["risk_level"] == "High"])

    email = f"""
Subject: Social Media Analysis Report

Hello,

Here is the summary of user data:

- Total Users: {len(df)}
- Average Age: {avg_age:.2f}
- High Risk Users: {high_risk}

Insight:
Users with higher addiction levels tend to fall into high-risk categories.

Regards,
Data Team
"""
    print(email)


# ---------------- CHATBOT ---------------- #

def chatbot():
    print("🤖 Smart Data Assistant")
    print("Commands:")
    print("summary | platform | bar | hist | scatter | line | email | exit")

    while True:
        cmd = input("\nYou: ").lower()

        if cmd == "summary":
            summary()

        elif cmd == "platform":
            platform_analysis()

        elif cmd == "bar":
            bar_graph()

        elif cmd == "hist":
            histogram()

        elif cmd == "scatter":
            scatter()

        elif cmd == "line":
            line_graph()

        elif cmd == "email":
            generate_email()

        elif cmd == "exit":
            print("Goodbye 👋")
            break

        else:
            print("Unknown command")


# Run chatbot
chatbot()