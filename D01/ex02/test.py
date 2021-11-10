from vector import Vector

def main():
    vector1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print("vect1 :")
    vector1.__repr__()
    print("")

    vector2 = Vector([0.0, 1.0, 2.0, 3.0])
    print("vect2 :")
    vector2.__repr__()
    print("")

    vector3 = Vector(4)
    print("vect3: ", vector3.values, vector3.shape)
    print("")

    vector4 = Vector((10,15))
    print("vect4: ", vector4.values, vector4.shape)
    print("")

    vector5 = Vector([0.0, 1.0, 2.0, 3.0])
    print("vect5: ", vector5.values, vector5.shape)
    print("")

 #   vectorinvalid = Vector(1, 2)
 #   vectorinvalid = Vector([1.0], [0.0], [2.0, 5])
 #   vectorinvalid = Vector([0.1, 0.2, 3])
 #   vectorinvalid = Vector(2.5)

    vector1.T()
    print("vect1: ", vector1.values, vector1.shape)
    print("")

    vector2.T()
    print("vect2: ", vector2.values, vector2.shape)
    print("")

    vector2.__add__(vector3)
    print("vect2: ", vector2.values, vector2.shape)
    print("")

    vector1.__add__(vector1)
    print("vect1: ", vector1.values, vector1.shape)
    print("")

    vector2.__sub__(vector3)
    print("vect2: ",vector2.values, vector2.shape)
    print("")

    vector1.__sub__(vector5)
    print("vect1: ",vector1.values, vector1.shape)
    print("")

    vector2.__sub__(vector3)
    print("vect2: ", vector2.values, vector2.shape)
    print("")

    vector1.__truediv__(2)
    print("vect1: ",vector1.values, vector1.shape)
    print("")

    vector3.__truediv__(2)
    print("vect3: ", vector3.values, vector3.shape)
    print("")

    vector1.__mul__(2)
    print("vect1: ",vector1.values, vector1.shape)
    print("")

    vector3.__mul__(2)
    print("vect3: ", vector3.values, vector3.shape)
    print("")

    print("{}".format(vector3.dot(vector2)))
    print("{}".format(vector1.dot(vector5)))

if __name__ == "__main__":
    main()