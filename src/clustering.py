from sklearn.cluster import KMeans


def elbow_method(X_scaled):
    wcss = []

    for i in range(1, 11):
        model = KMeans(
            n_clusters=i,
            random_state=42,
            n_init=10
        )

        model.fit(X_scaled)
        wcss.append(model.inertia_)

    return wcss


def train_model(X_scaled):
    model = KMeans(
        n_clusters=5,
        random_state=42,
        n_init=10
    )

    clusters = model.fit_predict(X_scaled)

    return model, clusters