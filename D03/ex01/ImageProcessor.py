import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os

class ImageProcessor():

    def load(self, path):
        if not os.path.isfile(path):
            print("Exception: FileNotFoundError -- strerror: No such file or directory")
            return None
        if os.path.getsize(path) == 0:
            print("Exception: OSError -- strerror: None")
            return None
        img = mpimg.imread(path)
        print("Loading image of dimensions {} x {}".format(img.shape[0], img.shape[1]))
        return img

    def display(self, array):
        if not isinstance(array, np.ndarray) or array is None:
            print("Display received a non numpy array variable or an empty numpy array")
            return None
        plt.axis('off')
        plt.imshow(array)
        plt.show()
