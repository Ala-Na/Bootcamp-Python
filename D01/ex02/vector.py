from operator import add, sub

class   Vector:

    def __init__(self, floats):
        self.values = []
        if isinstance(floats, int):
            self.__init_from_size__(floats)
        elif isinstance(floats, list):
            for elem in floats:
                if not isinstance(elem, list):
                    self.__init_from_list_of_float__(floats)
                    return
                else:
                    self.__init_from_list_of_list_of_float__(floats)
                    return
        elif isinstance(floats, tuple):
            self.__init_from_range__(floats)
        else:
            raise ValueError("{} not in correct format.".format(floats))

    def __init_from_list_of_float__(self, floats):
        for elem in floats:
            if isinstance(elem, float):
                self.values.append(elem)
            else:
                raise ValueError("{} is not in correct format.".format(elem))
        self.shape = (len(self.values), 1)

    def __init_from_list_of_list_of_float__(self, floats):
        for elem in floats:
            for sub_elem in elem:
                if not isinstance(sub_elem, float):
                    raise ValueError("{} is not in correct format.".format(sub_elem))
        for elem in floats:
            self.values.append(elem)
        self.shape = (1, len(self.values))

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
        self.shape = (self.shape[1], self.shape[0])
        for elem in self.values:
            if isinstance(elem, list):
                self.__T_row__()
                return
            else:
                self.__T_column__()
                return

    def __T_row__(self):
        new_values = []
        for elem in self.values:
           for sub_elem in elem:
               new_values.append(sub_elem)
        self.values = new_values

    def __T_column__(self):
        new_values = []
        for elem in self.values:
            sub_new_values = []
            sub_new_values.append(elem)
            new_values.append(sub_new_values)
        self.values = new_values

    def __add__(self, other):
        if not isinstance(other, Vector):
            self.__radd__(other)
            return
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
        self.values = new_values
        
    def __radd__(self, other):
        raise NotImplementedError("Vectors can only be additionned with other vectors.")

    def __sub__(self, other):
        if not isinstance(other, Vector):
            self.__rsub__(other)
            return
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
        self.values = new_values
        
    def __rsub__(self, other):
        raise NotImplementedError("Vectors can only be substracted with other vectors.")

    def __truediv__(self, other):
        if not isinstance(other, int) or other == 0:
            self.__rtruediv__(other)
            return
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
        self.values = new_values

    def __rtruediv__(self, other):
        if not isinstance(other, int):
            raise NotImplementedError("Only division with scalars are handled.")
        raise ZeroDivisionError("Can't divide by a zero !")

    def __mul__(self, other):
        if not isinstance(other, int):
            self.__rmul__(other)
            return
        new_values = []
        if isinstance(self.values[0], float):
            for elem in self.values:
                new_values.append(elem * other)
        else:
            for elem in self.values:
                for sub_elem in elem:
                    sub_new_values = []
                    sub_new_values.append(sub_elem * other)
                    new_values.append(sub_new_values)
        self.values = new_values

    def __rmul__(self, other):
        raise NotImplementedError("Only multiplication with scalars are handled.")

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