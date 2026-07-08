import matplotlib.pyplot as plt
import seaborn as sns


def plot_age_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["Age"], bins=15, kde=True)
    plt.title("Age Distribution")
    plt.show()


def plot_income_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["Annual Income (k$)"], bins=15, kde=True)
    plt.title("Annual Income Distribution")
    plt.show()


def plot_spending_distribution(df):
    plt.figure(figsize=(8,5))
    sns.histplot(df["Spending Score (1-100)"], bins=15, kde=True)
    plt.title("Spending Score Distribution")
    plt.show()