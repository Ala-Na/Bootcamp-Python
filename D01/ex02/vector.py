from operator import add, sub

class   Vector:

    def __init__(self, floats):
        self.values = []
        for elem in floats:
            for sub_elem in elem:
                if not isinstance(sub_elem, float):
                    raise ValueError("{} is not in correct format.".format(sub_elem))
        for elem in floats:
            self.values.append(elem)
        self.shape = (len(self.values), len(self.values[0]))

    def T(self):
        new_values = []
        if self.shape[0] == 1:
            for row in self.vector_list:
                for column in row:
                    new_values.append([column])
        else:
            sub_new_values = []
            for row in self.values:
                for col in row:
                    sub_new_values.append(col)
            new_values.append(sub_new_values)
        return Vector(new_values)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise NotImplementedError("Vectors can only be additionned with other vectors.")
        if len(self.values) != len(other.values):
            raise TypeError("Can't add two vectors of differents dimensions.")
        elif type(self.values[0]) != type(other.values[0]):
            raise TypeError("Can't add two vectors of differents dimensions.")
        new_values = []
        if isinstance(self.values[0], float):
            new_values = list(map(add, self.values, other.values))
        else:
            for elem, elem_ot in zip(self.values, other.values):
                new_values.append(list(map(add, elem, elem_ot)))
        return Vector(new_values)

    def __radd__(self, other):
        raise NotImplementedError("Vectors can only be additionned with other vectors.")

    def __sub__(self, other):
        if not isinstance(other, Vector):
          raise NotImplementedError("Vectors can only be substracted with other vectors.")
        if len(self.values) != len(other.values):
            raise TypeError("Can't substract two vectors of differents dimensions.")
        elif type(self.values[0]) != type(other.values[0]):
            raise TypeError("Can't substract two vectors of differents dimensions.")
        new_values = []
        if isinstance(self.values[0], float):
            new_values = list(map(sub, self.values, other.values))
        else:
            for elem, elem_ot in zip(self.values, other.values):
                new_values.append(list(map(sub, elem, elem_ot)))
        return Vector(new_values)

    def __rsub__(self, other):
        raise NotImplementedError("No substraction by vector.")

    def __truediv__(self, other):
        if not isinstance(other, int) and not (isinstance(other, float) and other.is_integer()):
            raise NotImplementedError("Only division with scalars are handled.")
        if other == 0:
            raise ZeroDivisionError("Can't divide by a zero !")
        new_values = []
        if isinstance(self.values[0], float):
            for elem in self.values:
                new_values.append(elem / other)
        else:
            for elem in self.values:
                for sub_elem in elem:
                    sub_new_values = []
                    sub_new_values.append(sub_elem / other)
                    new_values.append(sub_new_values)
        return Vector(new_values)

    def __rtruediv__(self, other):
        raise NotImplementedError("Can't divide by vector.")

    def __mul__(self, other):
        if not isinstance(other, int) or (isinstance(other, float) and not other.is_integer()):
            raise NotImplementedError("Only multiplication vectors with scalars are handled.")
        new_values = []
        if isinstance(self.values[0], float) or len(self.values[0]) == 1:
            for elem in self.values:
                new_values.append(elem * other)
        else:
            for elem in self.values:
                for sub_elem in elem:
                    sub_new_values = []
                    sub_new_values.append(sub_elem * other)
                    new_values.append(sub_new_values)
        return Vector(new_values)

    def __rmul__(self, other):
        self.__mul__(other)

    def __str__(self):
        txt = "{}".format(self.values)
        txt += "\t"
        txt += "{}".format(self.shape)
        return txt

    def __repr__(self):
        print("{}".format(self.__str__()))

    def dot(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Dot product can only be made from two vectors of same dimensions.")
        if len(self.values) != len(other.values):
            raise TypeError("Dot product can only be made from two vectors of same dimensions.")
        elif type(self.values[0]) != type(other.values[0]):
            raise TypeError("Dot product can only be made from two vectors of same dimensions.")
        res = 0
        if isinstance(self.values[0], float):
            for elem, oth_elem in zip(self.values, other.values):
                res += elem * oth_elem
        else:
            for elem, elem_ot in zip(self.values, other.values):
                for sub_elem, sub_elem_ot in zip(elem, elem_ot):
                    res += sub_elem * sub_elem_ot
        return res






#Column vectors : list of list of float
#Row vectors : list of float
#Shape for column : (nb_elem, 1)
#Shape for row : (1, nb_elem)

#Initialization :
#- List of float [f, f, f, f] (row)
#- List of lists of floats [[f], [f], [f], [f]] (column)
#- Size Vector(size) => [[f], [f], [f]] (column)
#- Range Vector((start, end)) => [[start], [f], [f], [end]] (column)
