class   Vector:

    def __init__(self, floats):
        self.values = []
        if isinstance(floats, int):

        elif ?range?:

        elif isinstance(floats, list):
            for elem in floats:
                if not isinstance(elem, list) and isinstance(elem, float):
                    self.values.append(elem)
                elif isinstance(elem,list):
                    for sub_elem in elem:
                        if not isinstance(sub_elem, float):
                            raise ValueError("{} is not a float.".format(sub_elem))
                    self.values.append(elem)
                else:
                    raise ValueError("{} is not correct format.")

    def __init_list_of_float__(self, floats):
        for elem in floats:
            if isinstance(elem, float):
                self.values.append(elem)
            else:
                raise ValueError("{} is not in correct format.", elem)


Column vectors : list of list of float 
Row vectors : list of float 
Shape for column : (nb_elem, 1)
Shape for row : (1, nb_elem)

Initialization :
- List of float [f, f, f, f] (column)
- List of lists of floats [[f], [f], [f], [f]] (column)
- Size Vector(size) => [[f], [f], [f]] (column)
- Range Vector((start, end)) => [[start], [f], [f], [end]] (column)