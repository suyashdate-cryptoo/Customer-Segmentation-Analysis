import pandas as pd
from sklearn.preprocessing import StandardScaler


def load_data(file_path):
    return pd.read_csv(file_path)


def preprocess_data(df):
    X = df[["Age", "Annual Income (k$)", "Spending Score (1-100)"]]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    return X, X_scaled, scaler