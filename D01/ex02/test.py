from vector import Vector

def main():
    vector1 = Vector([[0.0], [1.0], [2.0], [3.0]])
    print(vector1.values, vector1.shape)
    print("")

    vector2 = Vector([0.0, 1.0, 2.0, 3.0])
    print(vector2.values, vector2.shape)
    print("")

    vector3 = Vector(3)
    print(vector3.values, vector3.shape)
    print("")

    vector4 = Vector((10,15))
    print(vector4.values, vector4.shape)
    print("")

 #   vectorinvalid = Vector(1, 2)
 #   vectorinvalid = Vector([1.0], [0.0], [2.0, 5])
 #   vectorinvalid = Vector([0.1, 0.2, 3])
 #   vectorinvalid = Vector(2.5)

    vector1.T()
    print(vector1.values, vector1.shape)
    print("")

    vector2.T()
    print(vector2.values, vector2.shape)
    print("")

if __name__ == "__main__":
    main()