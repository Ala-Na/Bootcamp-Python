import numpy as np
import sys

from numpy.lib.arraysetops import isin
from numpy.ma.core import set_fill_value
from csvreader import CsvReader
import random
import matplotlib.pyplot as plt
import numpy as np

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def _get_init_centroids(self, X):
        for i in range(0, self.ncentroid):
            point = X[random.randint(0, len(X) - 1)]
            self.centroids.append(point)

    def _L1(self, centroid, point):
        if (len(centroid) != len (point)):
            print("Can't compare 2 vectors of differents dimensions")
            return -1
        return sum([abs(centroid[i] - point[i]) for i in range (len(centroid))])

    def _recalculate_centroids(self, old_centr, clusters, X):
        for centr_index in range(self.ncentroid):
            new_centr = [0.0] * len(X[0])
            if len(clusters[centr_index]) > 0:
                for point_index in clusters[centr_index]:
                    for elem in range(len(X[point_index])):
                        new_centr[elem] += X[point_index][elem]
                for divid in range(len(new_centr)):
                    new_centr[divid] /= len(clusters[centr_index])
                old_centr[centr_index] = new_centr
        return old_centr

    def _Kmeans_algo(self, X):
        self._get_init_centroids(X)
        ranges = [(min([row[i] for row in X]), max([row[i] for row in X])) for i in range(len(X[0]))]
        final_clusters = None
        for iter in range(self.max_iter):
            clusters = [[] for centr in range(self.ncentroid)]
            for elem in range(len(X)):
                point = X[elem]
                bestmatch = 0
                for centr_index in range(self.ncentroid):

                    distance = self._L1(self.centroids[centr_index], point)
                    if distance < self._L1(self.centroids[bestmatch], point):
                        bestmatch = centr_index
                clusters[bestmatch].append(elem)
            if clusters == final_clusters:
                break
            final_clusters = clusters
            self.centroids = self._recalculate_centroids(self.centroids, clusters, X)
        return clusters

    def predict(self, X):
        clusters = self._Kmeans_algo(X)
        vector_res = np.empty(X.shape[0])
        for index in range(len(clusters)):
            for citizen in clusters[index]:
                vector_res[citizen] = index
        return vector_res
        
    def _means_features(self, X, clusters):
        features =  [[] for area in range(self.ncentroid)]
        for list_index in range(self.ncentroid):
            mean_height = 0.0
            mean_weight = 0.0
            mean_density = 0.0
            for citizen in clusters[list_index]:
                mean_height += X[citizen][0]
                mean_weight += X[citizen][1]
                mean_density += X[citizen][2]
            mean_height /= len(clusters[list_index])
            mean_weight /= len(clusters[list_index])
            mean_density /= len(clusters[list_index])
            features[list_index].append(mean_height)
            features[list_index].append(mean_weight)
            features[list_index].append(mean_density)
        features_vector = np.array(features) 
        return features_vector

    def fit(self, X):
        clusters = self._Kmeans_algo(X)
        print(clusters)
        features = self._means_features(X, clusters)
        print(features)
        tallest = 0
        less_density = 0
        for area in range(len(features)):
            if features[area][0] > features[tallest][0]:
                tallest = area
            if features[area][2] < features[less_density][2]:
               less_density = area
        print(tallest)
        print(less_density)
        if tallest != less_density:
            diff_tall = features[tallest][0] - features[less_density][0]
            diff_dens = features[tallest][2] - features[less_density][2]
            print(diff_tall)
            print(diff_dens*100)
            if diff_tall > diff_dens*100:
                belt = tallest
            else:
                belt = less_density
        else:
            belt = tallest
        print(belt)
        return None

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