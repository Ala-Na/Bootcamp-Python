import numpy as np
import sys
from csvreader import CsvReader
import random
from sklearn.cluster import KMeans

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def predict(self, X):
        kmean = KMeans(n_clusters=self.ncentroid).predict(X)
        print(kmean.labels_)
        return kmean

    def fit(self, X):
        kmean = KMeans(n_clusters=self.ncentroid).fit(X)
        print(kmean.labels_)
        return kmean

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
    if (max_iter == -1 and ncentroid == -1):
        cluster = KmeansClustering()
    elif max_iter == -1:
        cluster = KmeansClustering(ncentroid=ncentroid)
    elif ncentroid == -1:
        cluster = KmeansClustering(max_iter=max_iter)
    else:
        cluster = KmeansClustering(ncentroid=ncentroid, max_iter=max_iter)
    cluster.fit(datas)