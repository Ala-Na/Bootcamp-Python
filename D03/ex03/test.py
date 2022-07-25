from ImageProcessor import ImageProcessor
imp = ImageProcessor()
arr = imp.load("../resources/elon_canaGAN.png")

from ColorFilter import ColorFilter

cf = ColorFilter()

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

grey = cf.to_grayscale(arr, 'm')
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'weight', weights = [0.2, 0.3, 0.5])
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'm')
if grey is not None:
    imp.display(grey)

grey = cf.to_grayscale(arr, 'w', lst=[0.30, 0.60, 0.10])
if grey is not None:
    imp.display(grey)
