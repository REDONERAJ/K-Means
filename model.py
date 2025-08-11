import pandas as pd
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import joblib

X, _ = make_blobs(
    n_samples=300,
    centers=3,
    n_features=3,
    cluster_std=1.2,
    random_state=42
)

features = ["Feature 1", "Feature 2", "Feature 3"]

df = pd.DataFrame(X, columns=features)

scaler = StandardScaler()
X_scaled = scaler.fit_transform(df)

kmeans = KMeans(n_clusters=3, n_init=20, random_state=42)
kmeans.fit(X_scaled)

joblib.dump((kmeans, scaler, features), 'synthetic_kmeans_model.pkl')
