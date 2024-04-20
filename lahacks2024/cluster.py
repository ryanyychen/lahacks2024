# necessary imports
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np

class Kmeans():
    """
    Static class for K-Means Clustering with given centroids
    """

    @staticmethod
    def cluster(df, centroids):
        """
        K-Means model initialization, run, and output

        Args:
            df (dataframe): dataframe of coordinates
            centroids (nparray): array of specified centroids
        """
        # setup K-means clustering and its parameters
        # init, n_init, max_iter are pulled from example notebook
        kmeans = KMeans(
            init = centroids,
            n_clusters = len(centroids),
            n_init = 1,
            max_iter = 100,
            random_state = 100
        )

        # run the model
        kmeans.fit(df)

        # returns dataframe of coordinates and their associated cluster
        return pd.DataFrame(kmeans.labels_)