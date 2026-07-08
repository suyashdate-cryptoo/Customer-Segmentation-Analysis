import pandas as pd


def save_csv(df, filename):
    df.to_csv(filename, index=False)


def cluster_summary(df):
    return df.groupby("Cluster")[
        ["Age", "Annual Income (k$)", "Spending Score (1-100)"]
    ].mean().round(2)