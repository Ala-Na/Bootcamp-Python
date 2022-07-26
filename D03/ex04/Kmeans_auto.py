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
        # features = self._means_features(X, clusters)
        # if (self.ncentroid != 4):
        #     for area in range(self.ncentroid):
        #         print("Area {:3} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
        #             .format(area + 1, len(clusters[area]), features[area][0], features[area][1], features[area][2]))
        # else:
        #     citizenship_index = self._get_citizenship(features)
        #     for area in range(self.ncentroid):
        #         print("{:27} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
        #             .format(citizenship_index[area], len(clusters[area]), features[area][0], features[area][1], features[area][2]))
        #     self._rep_citizens(X, clusters, features, citizenship_index)
        # return None
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
            if filepath is None:
                filepath = arg[len("filepath="):]
            else:
                print("More than 1 filepath given.")
                exit()
        if arg.startswith("ncentroid="):
            if ncentroid == -1:
                try:
                    ncentroid = (int)(arg[len("ncentroid="):])
                except:
                    print("Incorrect ncentroid argument")
                    exit()
            else:
                print("More than 1 ncentroid value given.")
                exit()
        if arg.startswith("max_iter="):
            if max_iter == -1:
                try:
                    max_iter = (int)(arg[len("max_iter="):])
                except:
                    print("Incorrect max_iter argument")
                    exit()
                if max_iter <= 0:
                    print("Incorrect max_iter argument")
                    exit()
            else:
                print("More than 1 max_iter value given.")
                exit()
    if not os.path.isfile(filepath):
        print("Error with filepath")
        exit()
    try:
        datas = np.genfromtxt(filepath, delimiter=',', skip_header=1, usecols=(1,2,3))
    except:
        print("File not valid")
        exit()
    if (max_iter == -1 and ncentroid == -1):
        cluster = KmeansClustering()
    elif max_iter == -1:
        cluster = KmeansClustering(ncentroid=ncentroid)
    elif ncentroid == -1:
        cluster = KmeansClustering(max_iter=max_iter)
    else:
        cluster = KmeansClustering(ncentroid=ncentroid, max_iter=max_iter)
    cluster.fit(datas)
