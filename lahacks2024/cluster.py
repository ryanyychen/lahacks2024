# necessary imports
from sklearn.cluster import KMeans
from k_means_constrained import KMeansConstrained
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
        kmeans = KMeans(
            init = centroids,
            n_clusters = len(centroids),
            n_init = 1,
            max_iter = 100,
            random_state = 0
        )

        # run the model
        kmeans.fit(df)

        # returns dataframe of coordinates and their associated cluster
        results = pd.DataFrame(kmeans.labels_)
        results.columns = ['cluster']
        return results

    @staticmethod
    def constrained_cluster(df, centroids):
        """
        K-Means model initialization with constrained cluster sizes, run, and output

        Args:
            df (dataframe): dataframe of coordinates
            centroids (nparray): array of specified centroids
        """
        # constant 4 passengers as its common passenger count for cars
        max_cluster_size = 4

        # setup constrained K-means clustering and its parameters
        kmeans = KMeansConstrained(
            init = centroids,
            n_clusters = len(centroids),
            size_min = 1,
            size_max = max_cluster_size,
            n_init = 1,
            max_iter = 100,
            random_state = 0
        )

        # run the model
        kmeans.fit(df)

        # returns dataframe of coordinates and their associated cluster
        results = pd.DataFrame(kmeans.labels_)
        results.columns = ['cluster']
        return results
