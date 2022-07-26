from typing import AsyncGenerator
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from numpy.lib import arrayterator
from numpy.lib.arraysetops import isin
from ImageProcessor import ImageProcessor

# Some infos about numpy array slicing and indexing :
# https://www.pythoninformer.com/python-libraries/numpy/index-and-slice/

class ColorFilter():

    def invert(self, array):
        if not isinstance(array, np.ndarray):
            return None
        invert_arr = array.copy()
        # Next step (slicing) is necessary as an image can have a RGBA channel and not only RGB
        for third_dim in range(3):
            invert_arr[:, :, third_dim] = 1 - array[:, :, third_dim]
        return invert_arr

    def to_blue(self, array):
        if not isinstance(array, np.ndarray):
            return None
        blue = np.zeros(array.shape)
        blue[:, :, 2:] = array[:, :, 2:]
        return blue

    def to_green(self, array):
        if not isinstance(array, np.ndarray):
            return None
        res = array * 1
        try :
            return res * [0, 1, 0, 1]
        except:
            return res * [0, 1, 0]

    def to_red(self, array):
        if not isinstance(array, np.ndarray):
            return None
        red = array.copy()
        green = self.to_green(array)
        blue = self.to_blue(array)
        for third_dim in range(3):
            red[:, :, third_dim] = array[:, :, third_dim] - green[:, :, third_dim] - blue[:, :, third_dim]
        return red

    def to_celluloid(self, array):
        if not isinstance(array, np.ndarray):
            return None
        res = 1 * array
        mask = np.linspace(0.0, 1.0, num=4)
        res[res > mask[2]] = mask[3]
        res[(res > mask[1]) & (res <= mask[2])] = mask[2]
        res[(res > mask[0]) & (res <= mask[1])] = mask[1]
        return res

    def _check_grayscale_arguments(self, filter, **kwargs):
        if not filter in ['m', 'mean', 'w', 'weight']:
            print("to_grayscale: incompatible filter.")
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
                if total < 0.99999 or total > 1.00001:
                    print("to_greyscale: sum of three floats values are not equal to 1.")
                    return False
        return True

    def to_grayscale(self, array, filter, **kwargs):
        if not isinstance(array, np.ndarray):
           return None
        if not self._check_grayscale_arguments(filter, **kwargs):
            return None
        rgb_weights = []
        if filter in ['m', 'mean']:
            rgb_weights = [1/3, 1/3, 1/3]
        else:
            for key, value in kwargs.items():
                rgb_weights = [value[0], value[1], value[2]]
        res = 1 * array
        gray = np.sum(array[:, :, :3] * rgb_weights, axis=(2))
        for third_dim in range(3):
            res[:, :, third_dim] = gray[:]
        return res
