### ml_dsl_project/src/ml_models/clustering.py
# Implementación del modelo de clustering K-means

from sklearn.cluster import KMeans

class ClusteringModel:
    def __init__(self, n_clusters=3):
        self.model = KMeans(n_clusters=n_clusters)

    def train(self, X):
        self.model.fit(X)
        print("Modelo K-means entrenado con éxito.")

    def predict(self, X):
        return self.model.predict(X)
