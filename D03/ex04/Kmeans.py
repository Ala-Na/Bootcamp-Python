from cmath import isnan
from re import A
import sys
from csvreader import CsvReader
import random
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import os

class KmeansClustering:

    def __init__(self, max_iter=20, ncentroid=4):
        self.ncentroid = ncentroid # number of centroids
        self.max_iter = max_iter # number of max iterations to update the centroids
        self.centroids = [] # values of the centroids

    def _get_init_centroids(self, X):
        self.centroids = []
        if (len(X) < self.ncentroid):
            print("Data input too small for ncentroid number.")
            exit()
        for i in range(0, self.ncentroid):
            point = X[random.randint(0, len(X) - 1)]
            while any((point == centr).all() for centr in self.centroids):
                point = X[random.randint(0, len(X) - 1)]
            self.centroids.append(point)

    # Manhattan distance (L1) is sum of absolute difference between 2 points
    # for each coordinate :
    # for a(x, y, ...) and b(x, y, ...)
    # d(a,b) = |x_b - x_a| + |y_b - y_a| + ...
    def _L1(self, centroid, point):
        if (len(centroid) != len (point)):
            print("Can't compare 2 vectors of differents dimensions")
            exit()
        return sum(abs(a - b) for a, b in zip(centroid, point))

    def _assignate_to_cluster(self, X):
        assignation = []
        for data in enumerate(X):
            for centr_idx in range(len(self.centroids)):
                distance = self._L1(self.centroids[centr_idx], data[1])
                if (centr_idx) == 0:
                    closest_centr_idx = centr_idx
                    closest_distance = distance
                if distance < closest_distance:
                    closest_distance = distance
                    closest_centr_idx = centr_idx
            assignation.append(closest_centr_idx)
        return assignation

    def _update_centroids(self, X, assignation):
        new_centr = []
        datas_per_centr = [[] for i in range(len(self.centroids))]
        for i in range(len(assignation)):
            datas_per_centr[assignation[i]].append(X[i])
        for centr in enumerate(datas_per_centr):
            if not centr[1]:
                mean = X[random.randint(0, len(X) - 1)]
            else:
                mean = np.mean(centr[1], axis=0)
            new_centr.append(mean)
        self.centroids = new_centr

    def _Kmeans_algo(self, X):
        self._get_init_centroids(X)
        prev_assignation = []
        for iter in range(self.max_iter):
            assignation = self._assignate_to_cluster(X)
            self._update_centroids(X, assignation)
            if (assignation == prev_assignation):
                break
            prev_assignation = assignation
        datas_per_centr = [[] for i in range(len(self.centroids))]
        for i in range(len(assignation)):
            datas_per_centr[assignation[i]].append(X[i])
        return (assignation, datas_per_centr)

    def predict(self, X):
        '''
        Predict from wich cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        the prediction has a numpy.ndarray, a vector of dimension m * 1.
        Raises:
        -------
        This function should not raise any Exception.
        '''
        assignations, clusters = self._Kmeans_algo(X)
        return assignations

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

    def _rep_citizens(self, X, clusters, citizenship_index):
        fig = plt.figure(figsize=(100,100))
        ax = plt.axes(projection='3d')
        mars_color = 'xkcd:crimson'
        label_mars = "Mars"
        venus_color = 'xkcd:olive'
        label_venus = "Venus"
        earth_color = 'xkcd:sky blue'
        label_earth = "Earth"
        belt_color = 'xkcd:golden yellow'
        label_belt = "Belt"
        ax.set_title('Citizens of Solar System',color='0.1')
        for i in range(len(citizenship_index)):
            for point in clusters[i]:
                if label_earth in citizenship_index[i]:
                    color = earth_color
                    label = label_earth
                elif label_mars in citizenship_index[i]:
                    color = mars_color
                    label = label_mars
                elif label_venus in citizenship_index[i]:
                    color = venus_color
                    label = label_venus
                else:
                    color = belt_color
                    label = label_belt
                ax.scatter(point[0], point[1], point[2], color=color)
        for feat in range(len(citizenship_index)):
            if "Earth" in citizenship_index[feat]:
                color = 'b'
                label = "Earth centroid"
            elif "Mars" in citizenship_index[feat]:
                color = 'r'
                label = "Mars centroid"
            elif "Venus" in citizenship_index[feat]:
                color = 'g'
                label = "Venus centroid"
            else:
                color = 'y'
                label = "Belt centroid"
            ax.scatter(self.centroids[feat][0], self.centroids[feat][1], self.centroids[feat][2], color=color, label=label, marker='*', s=100)
        custom_legend = [plt.Line2D([0], [0], marker='o', color=earth_color, label=label_earth), \
            plt.Line2D([0], [0], marker='o', color=belt_color, label=label_belt), \
            plt.Line2D([0], [0], marker='o', color=venus_color, label=label_venus), \
            plt.Line2D([0], [0], marker='o', color=mars_color, label=label_mars)]
        legend = ax.legend(handles=custom_legend, loc="upper right", title = "Citizens")
        centroid_legend = [plt.Line2D([0], [0], marker='*', color='b', label=label_earth), \
            plt.Line2D([0], [0], marker='*', color='y', label=label_belt), \
            plt.Line2D([0], [0], marker='*', color='g', label=label_venus), \
            plt.Line2D([0], [0], marker='*', color='r', label=label_mars)]
        ax.add_artist(legend)
        ax.legend(handles=centroid_legend, loc="lower left", title = "Centroid")
        ax.set_xlabel('Height(m)')
        ax.set_ylabel('Weight(kg)')
        ax.set_zlabel('Bone density(kg)')
        # plt.show()

    def fit(self, X):
        '''
        Run the K-means clustering algorithm.
        For the location of the initial centroids, random pick ncentroids from the dataset.
        Args:
        -----
        X: has to be an numpy.ndarray, a matrice of dimension m * n.
        Return:
        -------
        None.
        Raises:
        -------
        This function should not raise any Exception.
        '''
        assignations, clusters = self._Kmeans_algo(X)
        features = self.centroids
        if (self.ncentroid != 4):
            for area in range(self.ncentroid):
                print("Area {:3} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
                    .format(area + 1, len(clusters[area]), features[area][0], features[area][1], features[area][2]))
        else:
            citizenship_index = self._get_citizenship(features)
            for area in range(self.ncentroid):
                print("{:27} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
                    .format(citizenship_index[area], len(clusters[area]), features[area][0], features[area][1], features[area][2]))
            self._rep_citizens(X, clusters, citizenship_index)
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
