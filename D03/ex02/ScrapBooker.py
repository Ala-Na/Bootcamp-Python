import numpy as np

class ScrapBooker():

    def crop(self, array, dim, position=(0,0)):
        if not isinstance(array, np.ndarray) or \
            array is None:
            print("crop received a non numpy array as first argument.")
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or \
            not isinstance(dim[0], int) or not isinstance(dim[1], int):
            print("crop received a non tuple of two integers as second argument.")
            return None
        if not isinstance(position, tuple) or len(position) != 2 or \
            not isinstance(position[0], int) or not isinstance(position[1], int):
            print("crop received a non tuple of two integers as third argument.")
            return None
        if dim[0] > array.shape[0] or dim[1] > array.shape[1] or \
            (dim[0] + position[0]) > array.shape[0] or (dim[1] + position[1] > array.shape[1]):
            print("Can't crop outside of image dimensions.")
            return None
        img = array[position[0]:position[0] + dim[0], position[1]:position[1] + dim[1]]
        return img

    def thin(self, array, n, axis):
        if not isinstance(array, np.ndarray) or \
            array is None:
            print("thin received a non numpy array as first argument.")
            return None
        if not isinstance(n, int) or n <= 0:
            print("thin received a non positive integer as second argument.")
            return None
        if not isinstance(axis, int) or axis not in [0, 1]:
            print("thin received a non positive integer fit as axis as third argument.")
            return None
        if (axis == 0 and n > array.shape[0]) or (axis == 1 and n > array.shape[1]):
            print("Can't thin outside of image dimensions.")
            return None
        if axis == 0:
            axis = 1
        else:
            axis = 0
        return np.delete(array, list(range (n - 1, array.shape[axis], n)), axis=axis)

    def juxtapose(self, array, n, axis):
        if not isinstance(array, np.ndarray) or \
            array is None:
            print("thin received a non numpy array as first argument.")
            return None
        if not isinstance(n, int) or n <= 0:
            print("thin received a non positive integer as second argument.")
            return None
        if not isinstance(axis, int) or axis not in [0, 1]:
            print("thin received a non positive integer corresponding to axis as third argument.")
            return None
        if axis == 1:
            return np.tile(array, (1, n))
        return np.tile(array, (n, 1))

    def mosaic(self, array, dim):
        if not isinstance(array, np.ndarray) or \
            array is None:
            print("mosaic received a non numpy array as first argument.")
            return None
        if not isinstance(dim, tuple) or len(dim) != 2 or \
            not isinstance(dim[0], int) or not isinstance(dim[1], int):
            print("mosaic received a non tuple of two integers as second argument.")
            return None
        return np.tile(array, dim)
