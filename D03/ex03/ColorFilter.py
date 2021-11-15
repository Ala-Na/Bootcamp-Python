from typing import AsyncGenerator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy.lib import arrayterator
from numpy.lib.arraysetops import isin
from ImageProcessor import ImageProcessor

class ColorFilter():

    def invert(self, array):
        assert isinstance(array, np.ndarray), "invert received a non numpy array as argument."
        return (1 - array)
    
    def to_blue(self, array):
        assert isinstance(array, np.ndarray), "to_blue received a non numpy array as argument."
        blue = np.zeros(array.shape)
        blue[:, :, 2:] = array[:, :, 2:]
        return blue

    def to_green(self, array):
        assert isinstance(array, np.ndarray), "to_green received a non numpy array as argument."
        try :
            return array * [0, 1, 0, 1]
        except:
            return array * [0, 1, 0]

    def to_red(self, array):
        assert isinstance(array, np.ndarray), "to_red received a non numpy array as argument."
        return array - self.to_green(array) - self.to_blue(array)
    
    def to_celluloid(self, array):
        assert isinstance(array, np.ndarray), "to_celluloid received a non numpy array as argument."
        mask = np.linspace(0.0, 1.0, num=4)
        print(mask)
        array[array >= mask[3]] = mask[3]
        array[(array > mask[2]) & (array < mask[3])] = mask[2]
        array[(array > mask[1]) & (array < mask[2])] = mask[1]
        array[(array > mask[0]) & (array < mask[1])] = mask[0]
        array[(array <= mask[0])] = mask[0]
        return array

    def _check_grayscale_arguments(self, filter, **kwargs):
        if not filter in ['m', 'mean', 'w', 'weight']:
            print("to_grayscae: incompatible filter.")
            return False
        if filter in ['m', 'mean']:
            for elem in kwargs:
                if elem:
                    print("ft_grayscale: filter m/mean don't take any other arguments.")
                    return False
        if filter in ['w', 'weight']:
            if len(kwargs) != 1:
                print("to_greyscale: not enough or too much arguments for w/weight filter.")
                return False  
            for elem, value in kwargs.items(): 
                if not isinstance(value, list) or len(value) != 3:
                    print("to_greyscale: received a non list of three float as argument.")
                    return False 
                total = 0 
                for sub_value in value:
                    if not isinstance(sub_value, float):
                        print("to_greyscale: at least one argument is not a float for filter w/weight.")
                        return False
                    total += sub_value
                if total != 1:
                    print("to_greyscale: sum of three floats values are not equal to 1.")
                    return False
        return True

    def to_grayscale(self, array, filter, **kwargs):
        assert isinstance(array, np.ndarray), "to_grayscale received a non numpy array as argument."
        if not self._check_grayscale_arguments(filter, **kwargs):
            return None
        rgb_weights = []
        if filter in ['m', 'mean']:
            r = np.sum(array[:, :, 0])
            g = np.sum(array[:, :, 1])
            b = np.sum(array[:, :, 2])
            total = np.sum(array)
            rgb_weights = [r/total, g/total, b/total]
        else:
            for key, value in kwargs.items():
                rgb_weights = [value[0], value[1], value[2]]
        array[:, :, 0] *= rgb_weights[0]
        array[:, :, 1] *= rgb_weights[1]
        array[:, :, 2] *= rgb_weights[2]
        sm = np.sum(array, axis=2)
        print("Sum is {} || END".format(sm))
        ret = np.tile(sm[:, :, None], (1, 1, 3))
        return ret


imp = ImageProcessor()
cf = ColorFilter()
img = imp.load("../42AI.png")
arr = cf.to_grayscale(img, 'm')
if arr is not None:
    print(arr)
    imp.display(arr)
arr = cf.to_grayscale(img, 'w', lst=[0.30, 0.60, 0.10])
if arr is not None:
    print(arr)
    imp.display(arr)