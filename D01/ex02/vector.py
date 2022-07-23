from operator import add, sub

class   Vector:

    def __init__(self, floats):
        self.values = []
        if isinstance(floats, int):
            self.__init_from_size__(floats)
            return
        elif isinstance(floats, tuple):
            self.__init_from_range__(floats)
            return
        for elem in floats:
            for sub_elem in elem:
                if not isinstance(sub_elem, float):
                    raise ValueError("{} is not in correct format.".format(sub_elem))
        for elem in floats:
            self.values.append(elem)
        self.shape = (len(self.values), len(self.values[0]))

    def __init_from_size__(self, floats):
        elem = 0
        while elem < floats:
            sub_list = []
            sub_list.append(float(elem))
            self.values.append(sub_list)
            elem += 1
        self.shape = (1, len(self.values))

    def __init_from_range__(self, floats):
        i = 0
        for elem in floats:
            if not isinstance(elem, int) or i > 2:
                raise ValueError("{} is not in correct format.".format(elem))
            i += 1
        if (i != 2):
            raise ValueError("{} is not in correct format.".format(floats))
        for f in range(floats[0], floats[1]):
            sub_list = []
            sub_list.append(float(f))
            self.values.append(sub_list)
            f += 1
        self.shape = (1, len(self.values))

    def T(self):
        new_values = []
        if self.shape[0] == 1:
            for row in self.values:
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
        for row in self.values:
            sub_new_values = []
            for col in row:
                sub_new_values.append(col / other)
            new_values.append(sub_new_values)
        return Vector(new_values)

    def __rtruediv__(self, other):
        raise ArithmeticError("Can't divide by vector.")

    def __mul__(self, other):
        if not (isinstance(other, int) or isinstance(other, float)):
            raise NotImplementedError("Only multiplication vectors with scalars are handled.")
        new_values = []
        for row in self.values:
            sub_new_values = []
            for col in row:
                sub_new_values.append(col * other)
            new_values.append(sub_new_values)
        return Vector(new_values)

    def __rmul__(self, other):
        self.__mul__(other)

    def __str__(self):
        txt = "{}".format(self.values)
        return txt

    def __repr__(self):
        return self.__str__()

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
