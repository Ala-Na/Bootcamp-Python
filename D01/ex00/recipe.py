class Recipe:

    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if name and isinstance(name, str) and all(char.isalnum() or char.isspace() for char in name):
            self._name = name
        else:
            raise ValueError("Name is not a string or doesn't contains only alphabetic and spaces characters.")


    @property
    def cooking_lvl(self):
        return self._cooking_lvl
    
    @cooking_lvl.setter
    def cooking_lvl(self, cooking_lvl):
        if isinstance(cooking_lvl, int) and cooking_lvl in range (1, 5):
            self._cooking_lvl = cooking_lvl
        else:
            raise ValueError("Cooking level difficulty is out of range (1 to 5).")


    @property
    def cooking_time(self):
        return self._cooking_time
    
    @cooking_time.setter
    def cooking_time(self, cooking_time):
        if isinstance(cooking_time, int) and cooking_time >= 0:
            self._cooking_time = cooking_time
        else:
            raise ValueError("Cooking time can't be negative.")


    @property
    def ingredients(self):
        return self._ingredients
    
    @ingredients.setter
    def ingredients(self, ingredients):
        if isinstance(ingredients, list):
            for elem in ingredients:
                if not elem or not isinstance(elem, str):
                    raise ValueError("At least one element in ingredients is not a string.")
            self._ingredients = ingredients
        else:
            raise ValueError("Ingredients is not a list.")


    @property
    def description(self):
        return self._description
    
    @description.setter
    def description(self, description):
        if isinstance(description, str):
            self._description = description
        else:
            raise ValueError("Description is not a string.")
    

    @property
    def recipe_type(self):
        return self._recipe_type

    @recipe_type.setter
    def recipe_type(self, recipe_type):
        valid_types = ['starter', 'lunch', 'dessert']
        if isinstance(recipe_type, str) and recipe_type in valid_types:
            self._recipe_type = recipe_type
        else:
            raise ValueError("Recipe type in unknown.")


    def __str__(self):
        txt = "\nRecipe for {}:\n{}\n".format(self.name, self.description)
        txt += "Type: {}\tDifficulty level: {}\tCooking time: {} minutes\n".format(self.recipe_type, self.cooking_lvl, self.cooking_time)
        txt += "Ingredients list: {}\n".format(self.ingredients)
        return txt
