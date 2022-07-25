import numpy as np
import random

from numpy.core.fromnumeric import nonzero
from numpy.lib.arraysetops import isin

class   NumPyCreator():

    def from_list(self, lst, dtype=None):
        if not isinstance(lst, list):
            return None
        if len(lst) != 0 and isinstance(lst[0], list):
            for row in lst:
                if len(row) != len(lst[0]):
                    return None
        return np.asarray(lst, dtype=dtype)

    def from_tuple(self, tpl, dtype=None):
        if not isinstance(tpl, tuple):
            return None
        if len(tpl) != 0 and isinstance(tpl[0], tuple):
            for row in tpl:
                if len(row) != len(tpl[0]):
                    return None
        return np.asarray(tpl, dtype=dtype)

    def from_iterable(self, itr, dtype=None):
        if not iter(itr):
            return None
        return np.fromiter(itr, dtype=dtype)

    def from_shape(self, shape, value = 0, dtype=None):
        if not isinstance(shape, tuple) or len(shape) != 2 or shape[0] < 0 or shape[1] < 0:
            return None
        return np.full(shape, value, dtype=dtype)

    def random(self, shape, dtype=None):
        if not isinstance(shape, tuple) or len(shape) != 2 or shape[0] < 0 or shape[1] < 0:
            return None
        return np.random.rand(*shape).astype(dtype)

    def identity(self, n, dtype=None):
        if not isinstance(n, int) or n < 0:
            return None
        return np.identity(n, dtype=dtype)
