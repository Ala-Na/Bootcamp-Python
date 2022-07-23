from book import Book
from recipe import Recipe

def main():
    book = Book("Cookbook")
    tourte = Recipe("tourte", 2, 120, ['pate', 'legumes', 'viande'], "A classic tourte recipe", "lunch")
    fromage =  Recipe("fromage", 4, 60, ['lait', 'ferment'], "It smell bad", "dessert")
    # omelettefromage =  Recipe("omelette du fromage", 56, 60, ['lait', 'ferment'], "It smell bad", "dessert")
    pates = Recipe("pates", 1, 20, ['pates', 'eau'], "Pretty easy", 'lunch')

    print("Check __str__ of a recipe:")
    print ("---")
    print(pates)
    print("---\n")

    print("Check book creation")
    print ("---")
    print("\nBook was created at {} and modified at {}".format(book.creation_date, book.last_update))
    print("---")
    print("Book was created. Adding not existing recipe.\n")
    print("---")
    book.add_recipe("existpa")
    print("---\n")

    print("Adding recipe.\n")
    print("---")
    book.add_recipe(tourte)
    print("---\n")

    print("Display recipes names by type")
    print("---")
    book.get_recipes_by_types('starter')
    book.get_recipes_by_types('lunch')
    book.get_recipes_by_types('dessert')
    print("---\n")

    print("\nAdding existing recipe. And display recipes by name")
    print("---")
    book.add_recipe(fromage)
    book.get_recipes_by_types('bonbon')
    book.get_recipes_by_types('dessert')
    print("---\n")

    print("\nGet recipe by name.")
    print("---")
    book.get_recipe_by_name("tourte")
    book.get_recipe_by_name("fromage")
    print("---\n")

    print("Display recipes names by type")
    print("---")
    book.get_recipes_by_types('starter')
    book.get_recipes_by_types('lunch')
    book.get_recipes_by_types('dessert')
    print("---\n")

    print("Check of book modification")
    print("---")
    print("Book was created at {} and modified at {}".format(book.creation_date, book.last_update))
    print("---\n")

if __name__ == "__main__":
    main()
