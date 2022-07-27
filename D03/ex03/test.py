import numpy as np
import matplotlib
from matplotlib import pyplot as plt

from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("../resources/elon_canaGAN.png")

from ColorFilter import ColorFilter

cf = ColorFilter()
imp.display(arr)

invert = cf.invert(arr)
if invert is not None:
    imp.display(invert)

green = cf.to_green(arr)
if green is not None:
    imp.display(green)

red = cf.to_red(arr)
if red is not None:
    imp.display(red)

blue = cf.to_blue(arr)
if blue is not None:
    imp.display(blue)

cell = cf.to_celluloid(arr)
if cell is not None:
    imp.display(cell)

invert = cf.invert(1)
if invert is not None:
    imp.display(invert)

green = cf.to_green(1)
if green is not None:
    imp.display(green)

red = cf.to_red(1)
if red is not None:
    imp.display(red)

blue = cf.to_blue(1)
if blue is not None:
    imp.display(blue)

cell = cf.to_celluloid(1)
if cell is not None:
    imp.display(cell)

grey = cf.to_grayscale(arr, 'm')
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'weight', weights = [1.0, 0.0, 0.0])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'mean')
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'w', lst=[0.30, 0.60, 0.10])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'mean', lst=[0.30, 0.60, 0.10])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'w')
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'w', lst=[0.30, 0.00, 0.10])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'w', lst=[0.30, 'lol', 0.10])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'w', lst=[0.30, 0.00, 0.10, 0.60])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale('trololo', 'm')
if grey is not None:
    imp.display(grey)
else:
    print("arr was not a numpy array")

# Github tests

for f in [cf.to_red, cf.to_green, cf.to_blue, cf.invert]:
	array = plt.imread("../resources/elon_canaGAN.png")
	plt.imshow(f(array))
	plt.show()

im = cf.to_grayscale(array, "m")
plt.imshow(im, cmap="gray")
plt.show()

im = cf.to_grayscale(array, "w", weights = [0.2126, 0.7152, 0.0722])
plt.imshow(im, cmap="gray")
plt.show()
