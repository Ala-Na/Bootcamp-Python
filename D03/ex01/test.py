from ImageProcessor import ImageProcessor

print("Non functionnal test\n------------------")
imp = ImageProcessor()
arr = imp.load("non_existing_file.png")
print(arr)

print("")

arr = imp.load("empty_file.png")
print(arr)

print("\nFunctionnal test\n------------------")
imp = ImageProcessor()
arr = imp.load("../resources/42AI.png")
if arr is not None:
    print(arr, arr.dtype)
    imp.display(arr)
