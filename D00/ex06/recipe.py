import sys

cookbook = {
    'sandwich':  {
        'ingredients' : ['ham', 'bread', 'cheese', 'tomatoes'],
        'meal' : 'lunch',
        'prep_time' : '10'
    },
    'cake':   {
        'ingredients' : ['flour', 'sugar', 'eggs'],
        'meal' : 'dessert',
        'prep_time' : '60'
    },
    'salad': {
        'ingredients' : ['avocado', 'aragula', 'tomatoes', 'spinach'],
        'meal' : 'lunch',
        'prep_time' : '15'
    }
}

def printRecipe(key):
    if key not in cookbook.keys():
        print("No recipe named {} present in cookbook".format(key))
        return
    print("\nRecipe for {}:".format(key))
    print("Ingredients list: {}".format(cookbook[key].get('ingredients')))
    print("To be eaten for {}.".format(cookbook[key].get('meal')))
    print("Takes {} minutes for cooking.".format(cookbook[key].get('prep_time')))
    print("...\n")

def prepPrintRecipe():
    key = getRecipeKeyOrValue("\nPlease enter the recipe's name to get its details")
    printRecipe(key)

def getRecipeKeyOrValue(string):
    print(string)
    key = ""
    while not key:
        key = input(">> ").lower()
    return key

def getIngredientsList():
    print("\nEnter list of ingredients: (enter end to finish the list)")
    ingredient_list = []
    while True:
        ingredient = ""
        while not ingredient:
            ingredient = input(">> ").lower()
        if (ingredient == 'end'):
            break
        ingredient_list.append(ingredient)
    return ingredient_list

def printCookbook():
    print("\nRecipes present in cookbook:")
    if not cookbook:
        print("Cookbook is empty\n")
        return
    for key,value in cookbook.items():
        print("{}".format(key.capitalize()), end='')
        if key != list(cookbook)[-1]:
            print(", ", end='')
    print("\n")

def deleteRecipe(key):
    if key not in cookbook.keys():
        print("No recipe named {} present in cookbook\n".format(key))
        return
    del cookbook[key]
    print("\nRecipe {} erased from cookbook\n".format(key))

def prepDeleteRecipe():
   key = getRecipeKeyOrValue("Please enter recipe's name to erase").lower()
   deleteRecipe(key)

def AddRecipe(key, ingredient_list, meal_type, time):
    cookbook[key] = {}
    cookbook[key]['ingredients'] = ingredient_list
    cookbook[key]['meal'] = meal_type
    cookbook[key]['prep_time'] = time
    print("\nRecipe {} successfully added to cookbook".format(key))

def prepAddRecipe():
    key = getRecipeKeyOrValue("\nPlease enter new recipe's name:")
    ingredient_list = getIngredientsList()
    meal_type = getRecipeKeyOrValue("\nEnter type of meal:")
    time = getRecipeKeyOrValue("\nEnter preparation time in minutes:")
    AddRecipe(key, ingredient_list, meal_type, time)

def printMenu():
    print("Please select an option by typing the corresponding number:")
    print("1: Add a recipe")
    print("2: Delete a recipe")
    print("3: Print a recipe")
    print("4: Print the cookbook")
    print("5: Quit")

def Quit():
    print("\nCookbook closed.")
    sys.exit()

while True:
    printMenu()
    option = input(">> ")
    if option == "1":
        prepAddRecipe()
    elif option == "2":
        prepDeleteRecipe()
    elif option == "3":
        prepPrintRecipe()
    elif option == "4":
        printCookbook()
    elif option == "5":
        Quit()
    else:
        print("\nThis option does not exist, please type the corresponding number.")
        print("To exit, enter 5.")
        print("...\n")