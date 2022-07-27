import numpy as np
import sys
from csvreader import CsvReader
import random
from sklearn.cluster import KMeans
import os

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def _get_citizenship(self, features):
        tallest = 0
        less_density = 0
        thinest = 0
        for area in range(len(features)):
            if features[area][0] > features[tallest][0]:
                tallest = area
            if features[area][2] < features[less_density][2]:
               less_density = area
        if tallest != less_density:
            diff_tall = features[tallest][0] - features[less_density][0]
            diff_dens = features[tallest][2] - features[less_density][2]
            if diff_tall > diff_dens*100:
                belt = tallest
            else:
                belt = less_density
        else:
            belt = tallest
        if belt != 0:
            tallest = 0
        else:
            tallest = 1
            thinest = 1
        for area in range(len(features)):
            if features[area][0] > features[tallest][0] and area != belt:
                tallest = area
            if features[area][1] < features[thinest][1] and area != belt:
                thinest = area
        if tallest != thinest:
            venus = thinest
            mars = tallest
        else:
            venus = thinest
            mars = -1
        if (belt == 0 and venus == 1) or (belt == 1 or venus == 0):
            tallest = 2
        elif belt == 0 or venus == 0:
            tallest = 1
        else:
            tallest = 0
        for area in range(len(features)):
            if features[area][0] > features[tallest][0] and area != belt and area != venus:
                tallest = area
        mars = tallest
        for area in range(len(features)):
            if area != belt and area != venus and area != mars:
                earth = area
        citizenship_index = ["" for x in range(len(features))]
        for area in range(len(features)):
            if area == earth:
                citizenship_index[area] = 'United Nations of Earth'
            elif area == mars:
                citizenship_index[area] = 'Mars Republic'
            elif area == venus:
                citizenship_index[area] = 'The flying cities of Venus'
            else:
                citizenship_index[area] = 'Ateroids\' Belt colonies'
        return citizenship_index

    def predict(self, X):
        kmean = KMeans(n_clusters=self.ncentroid, max_iter=self.max_iter).fit_predict(X)
        return kmean

    def fit(self, X):
        kmean = KMeans(n_clusters=self.ncentroid, max_iter=self.max_iter).fit(X)
        features = kmean.cluster_centers_
        nb = [0] * self.ncentroid
        for i in range(len(kmean.labels_)):
            nb[kmean.labels_[i]] += 1
        if (self.ncentroid != 4):
            for area in range(self.ncentroid):
                print("Area {:3} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
                    .format(area + 1, nb[area], features[area][0], features[area][1], features[area][2]))
        else:
            citizenship_index = self._get_citizenship(features)
            for area in range(self.ncentroid):
                print("{:27} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
                    .format(citizenship_index[area], nb[area], features[area][0], features[area][1], features[area][2]))
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
                if (ncentroid <= 0):
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
    print(cluster.predict(datas))
