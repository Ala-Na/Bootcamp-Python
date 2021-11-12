import numpy
import random

class   NumPyCreator():

    def from_list(self, lst, *args):
        if not args and isinstance(lst, list):
            dtype=object
            if isinstance(lst[0], list):
                size = -1
                for row in lst:
                    if size == -1:
                        size = len(row)
                    if len(row) != size:
                        print("from_list received list containing elements of differents sizes.")
                        return None
                    if any(isinstance(elem, str) for elem in row):
                        dtype='<U21'
            if any(isinstance(value, str) for value in lst):
                dtype='<U21'
            array = numpy.asarray(lst, dtype=dtype)
            return array
        else:
            print("from_list received a non list argument.")
            return None

    def from_tuple(self, tpl):
        if isinstance(tpl, tuple):
            return numpy.asarray(tpl)
        else:
            print("from_tuple received a non tuple argument.")
            return None

    def from_iterable(self, itr):
        try:
            iterator = iter(itr)
            return numpy.fromiter(itr, int)
        except:
            print("from_iterable received a non iterable argument.")
            return None

    def from_shape(self, shape, value = 0):
        if isinstance(shape, tuple):
            return numpy.full(shape, value)
        else:
            print("from_shape received a non tuple argument.")
            return None

    def random(self, shape):
        if isinstance(shape, tuple):
            return numpy.random.rand(*shape)
        else:
            print("random received a non tuple argument.")
            return None

    def identity(self, n):
        if isinstance(n, int):
            return numpy.identity(n)
        else:
            print("identity received a non integer argument.")
            return None
