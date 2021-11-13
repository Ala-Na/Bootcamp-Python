import numpy as np
import random

from numpy.core.fromnumeric import nonzero
from numpy.lib.arraysetops import isin

class   NumPyCreator():

    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return None
        if isinstance(lst[0], list):
            for row in lst:
                if len(row) != len(lst[0]):
                    return None
        return np.asarray(lst,dtype=object)

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        return np.asarray(tpl)

    def from_iterable(self, itr, dtype=None):
        if not iter(itr):
            return None
        return np.fromiter(itr, dtype)

    def from_shape(self, shape, value = 0, dtype=None):
        return np.full(shape, value, dtype=dtype)

    def random(self, shape, dtype=None):
        return np.random.rand(*shape).astype(dtype)

    def identity(self, n, dtype=None):
        return np.identity(n, dtype=dtype)
