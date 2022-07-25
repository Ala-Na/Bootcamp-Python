import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()

arr1 = np.arange(0,25).reshape(5,5)
print("Array: \n{}\n".format(arr1))
arr1 = spb.crop(arr1, (3,1),(1,0))
print("After crop: \n{}\n".format(arr1))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
print("Array: \n{}\n".format(arr2))
arr2 = spb.thin(arr2,3,0)
print("After thin: \n{} dtype={}\n".format(arr2, arr2.dtype))

arr2 = np.array("A B C D E F G H I".split() * 6).reshape(9,-1)
print("Array: \n{}\n".format(arr2))
arr2 = spb.thin(arr2,3,1)
print("After thin: \n{} dtype={}\n".format(arr2, arr2.dtype))

arr3 = np.array([[1, 2, 3],[1, 2, 3],[1, 2, 3]])
print("Array: \n{}\n".format(arr3))
arr3 = spb.juxtapose(arr3, 3, 1)
print("After juxtapose: \n{}\n".format(arr3))

arr4 = np.array([[1, 2],[3, 4]])
print("Array: \n{}\n".format(arr4))
arr4 = spb.mosaic(arr4, (4, 4))
print("After mosaic: \n{}\n".format(arr4))

print("Errors checks:")
not_numpy_arr = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
spb.crop(not_numpy_arr, (1,2))
spb.juxtapose(arr4, -2, 0)
spb.mosaic(arr4, (1, 2, 3))
