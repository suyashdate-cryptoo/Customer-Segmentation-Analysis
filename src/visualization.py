import matplotlib.pyplot as plt
import seaborn as sns


def plot_customer_segments(df, centroids):
    plt.figure(figsize=(10,7))

    sns.scatterplot(
        data=df,
        x="Annual Income (k$)",
        y="Spending Score (1-100)",
        hue="Cluster",
        palette="Set1",
        s=100
    )

    plt.scatter(
        centroids[:,1],
        centroids[:,2],
        c="black",
        marker="X",
        s=300
    )

    plt.title("Customer Segments")
    plt.show()