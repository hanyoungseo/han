import pandas as pd
import numpy as np

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def create_customer_data(count=300):
    np.random.seed(10)

    data = {
        "age": np.random.randint(20, 65, count),
        "income": np.random.randint(2000, 10000, count),
        "purchase_count": np.random.randint(1, 50, count),
        "average_purchase": np.random.randint(10000, 500000, count)
    }

    return pd.DataFrame(data)


def preprocess_data(df):
    features = [
        "age",
        "income",
        "purchase_count",
        "average_purchase"
    ]

    scaler = StandardScaler()

    scaled_data = scaler.fit_transform(df[features])

    return scaled_data


def perform_clustering(data, clusters=4):
    model = KMeans(
        n_clusters=clusters,
        random_state=42,
        n_init=10
    )

    labels = model.fit_predict(data)

    return model, labels


def analyze_clusters(df):
    summary = df.groupby("cluster").agg({
        "age": "mean",
        "income": "mean",
        "purchase_count": "mean",
        "average_purchase": "mean"
    })

    return summary


def main():
    customers = create_customer_data()

    print("Customer Data")
    print(customers.head())

    scaled_data = preprocess_data(customers)

    model, labels = perform_clustering(
        scaled_data,
        clusters=4
    )

    customers["cluster"] = labels

    cluster_summary = analyze_clusters(customers)

    print("\n===== Cluster Summary =====")
    print(cluster_summary.round(2))

    print("\nCluster distribution")
    print(customers["cluster"].value_counts())

    customers.to_csv(
        "customer_clusters.csv",
        index=False
    )

    print("\nFile saved: customer_clusters.csv")


if __name__ == "__main__":
    main()
