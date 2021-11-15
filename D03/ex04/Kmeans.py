import numpy as np
import sys
from csvreader import CsvReader
import random
import matplotlib.pyplot as plt

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        #... parameters control...
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def _get_init_centroids(self, X):
        centroids = []
        for i in range(0, self.ncentroid):
            point = X[random.randint(0, len(X) - 1)]
            centroids.append(point)
        return centroids

    def fit(self, X):
        centroids = self._get_init_centroids(X)
        print(centroids)
        """
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        None.
        Raises:
        This function should not raise any Exception.
        """
        #... your code ...
        pass

    def predict(self, X):
        """
        Predict from wich cluster each datapoint belongs to.
        Args:
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Returns:
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        This function should not raise any Exception.
        """
        #... your code ...
        pass

def check_argument(*args):
    if (len(args) <= 1 or len(args) > 4):
        print("Incompatible number of arguments !")
        exit()
    if not any(arg.startswith("filepath=") for arg in args):
        print("Missing filepath !")
        exit()
    if (len(args) == 3 and (not any(arg.startswith("ncentroid") for arg in args) and not any(arg.startswith("max_iter") for arg in args)))\
        or (len(args) == 4 and (not any(arg.startswith("ncentroid") for arg in args) or not any(arg.startswith("max_iter") for arg in args))):
        print("Unknown argument !")
        exit()
    return

if __name__ == "__main__":
    check_argument(*sys.argv)
    filepath = None
    ncentroid = -1
    max_iter = -1
    for arg in sys.argv:
        if arg.startswith("filepath="):
            if not filepath:
                filepath = arg[len("filepath="):]
            else:
                print("More than 1 filepath given.")
                exit()
        if arg.startswith("ncentroid="):
            if ncentroid == -1:
                ncentroid = (int)(arg[len("ncentroid="):])
            else:
                print("More than 1 ncentroid value given.")
                exit()
        if arg.startswith("max_iter="):
            if max_iter == -1:
                max_iter = (int)(arg[len("max_iter="):])
            else:
                print("More than 1 max_iter value given.")
                exit()
    datas = np.genfromtxt(filepath, delimiter=',', skip_header=1, usecols=(1,2,3))
    if (max_iter == -1 and iter == -1):
        cluster = KmeansClustering()
    elif max_iter == -1:
        cluster = KmeansClustering(ncentroid=ncentroid)
    elif ncentroid == -1:
        cluster = KmeansClustering(max_iter=max_iter)
    else:
        cluster = KmeansClustering(ncentroid=ncentroid, max_iter=max_iter)
    cluster.fit(datas)