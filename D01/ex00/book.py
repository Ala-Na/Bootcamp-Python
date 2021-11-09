from recipe import Recipe
import datetime

class   Book:

    def __init__(self, name):
        self.name = name
        self.creation_date = datetime.datetime.now()
        self.last_update = self.creation_date
        self.recipes_list = {'starter' : [], 'lunch' : [], 'dessert' : []}

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name and isinstance(name, str) and all(char.isalnum() or char.isspace() for char in name):
            self._name = name
        else:
            raise ValueError("Name is not a string or doesn't contains only alphabetic and spaces characters.")

    def get_recipe_by_name(self, name):
        for key,values in self.recipes_list.items(): 
            for elem in values:
                if elem.name == name:
                    print(str(elem))
                    return elem
        print("{} not present in {}.".format(name, self.name))

    def get_recipes_by_types(self, recipe_type):
        if recipe_type not in self.recipes_list.keys():
            print("{} is not a valid recipe type.".format(recipe_type))
            return
        print("{} recipes :".format(recipe_type.capitalize()))
        for recipe in self.recipes_list[recipe_type]:
            print("{}".format(recipe.name))
        pass

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            print("You can only add objects of Recipe class inside {}.".format(self.name))
            return
        self.last_update = datetime.datetime.now()
        self.recipes_list[recipe.recipe_type].append(recipe)
        pass
