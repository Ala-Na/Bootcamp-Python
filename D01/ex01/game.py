class   GotCharacter:

    def __init__(self, first_name, is_alive):
        self.first_name = first_name
        self.is_alive = True

class   Targaryen(GotCharacter):

    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Targaryen"
        self.house_words = "Fire and Blood"
        self.__doc__ = "A class representing the Targaryen family. Or when cosanguinity is far too high."

    def print_house_words(self):
        print("{} !!!".format(self.house_words.upper()))
        pass

    def die(self):
        self.is_alive = False
        pass
