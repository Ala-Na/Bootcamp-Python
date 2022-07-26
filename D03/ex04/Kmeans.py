
import sys
from csvreader import CsvReader
import random
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
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

    def _rep_citizens(self, X, clusters, features, citizenship_index):
        vector_res = [-1] * len(X)
        for index in range(len(clusters)):
            for citizen in clusters[index]:
                vector_res[citizen] = index
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
        for point in range(len(X)):
            if label_earth in citizenship_index[vector_res[point]]:
                color = earth_color
                label = label_earth
            elif label_mars in citizenship_index[vector_res[point]]:
                color = mars_color
                label = label_mars
            elif label_venus in citizenship_index[vector_res[point]]:
                color = venus_color
                label = label_venus
            else:
                color = belt_color
                label = label_belt
            ax.scatter(X[point][0], X[point][1], X[point][2], color=color)
        for feat in range(len(features)):
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
            ax.scatter(features[feat][0], features[feat][1], features[feat][2], color=color, label=label)
        custom_legend = [plt.Line2D([0], [0], marker='o', color=earth_color, label=label_earth), \
            plt.Line2D([0], [0], marker='o', color=belt_color, label=label_belt), \
            plt.Line2D([0], [0], marker='o', color=venus_color, label=label_venus), \
            plt.Line2D([0], [0], marker='o', color=mars_color, label=label_mars)]
        legend = ax.legend(handles=custom_legend, loc="upper right", title = "Citizens")
        centroid_legend = [plt.Line2D([0], [0], marker='o', color='b', label=label_earth), \
            plt.Line2D([0], [0], marker='o', color='y', label=label_belt), \
            plt.Line2D([0], [0], marker='o', color='g', label=label_venus), \
            plt.Line2D([0], [0], marker='o', color='r', label=label_mars)]
        ax.add_artist(legend)
        ax.legend(handles=centroid_legend, loc="lower left", title = "Centroid")
        plt.show()

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
        clusters = self._Kmeans_algo(X)
        features = self._means_features(X, clusters)
        if (self.ncentroid != 4):
            for area in range(self.ncentroid):
                print("Area {:3} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
                    .format(area + 1, len(clusters[area]), features[area][0], features[area][1], features[area][2]))
        else:
            citizenship_index = self._get_citizenship(features)
            for area in range(self.ncentroid):
                print("{:27} : Total of {:3} citizens, with mean heigh of {:6.2f}, mean weight of {:6.2f} and mean bone density of {:4.2f}."\
                    .format(citizenship_index[area], len(clusters[area]), features[area][0], features[area][1], features[area][2]))
            self._rep_citizens(X, clusters, features, citizenship_index)
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
    cluster.predict(datas)
