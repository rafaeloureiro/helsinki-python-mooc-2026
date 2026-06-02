"""
A program which allows the user to search for recipes based on their names, preparation times, or ingredients used. 
The program should read the recipes from a file submitted by the user.
Each recipe consists of three or more lines. 
The first line has the name of the recipe, the second line contains an integer number representing the preparation time in minutes, and the remaining line or lines contain the ingredients used, one on each line. 
The recipe ends with an empty line, with the exception of the final recipe in the file which just ends with the end of the file. So, there can be more than one recipe in a single file, like in the example below.
"""


"""
PART 01
Search for recipes based on the name of the recipe
Please write a function named search_by_name(filename: str, word: str), which takes a filename and a search string as its arguments. 
The function should go through the file and select all recipes whose name contains the given search string. 
The names of these recipes are then returned in a list.
"""

def load_recipes(filename: str):
    with open(filename) as file:
        lines = [line.strip() for line in file]

    recipes = []
    i = 0
    while i < len(lines):
        if lines[i] == "":
            i += 1
            continue
        name = lines[i]
        time = int(lines[i + 1])
        ingredients = []
        i += 2
        while i < len(lines) and lines[i] != "":
            ingredients.append(lines[i])
            i += 1
        recipes.append({"name": name, "time": time, "ingredients": ingredients})
    return recipes

def search_by_name(filename: str, word: str):
    recipes = load_recipes(filename)
    found = []
    for recipe in recipes:
        if word.lower() in recipe["name"].lower():
            found.append(recipe["name"])
    return found

"""
A function named search_by_time(filename: str, prep_time: int), which takes a filename and an integer as its arguments. 
The function should go through the file and select all recipes whose preparation time is at most the number given.
The names of these recipes are again returned in a list, but the preparation time should be appended to each name.
"""

def search_by_time(filename: str, max_time: int):
    recipes = load_recipes(filename)
    found = []
    for recipe in recipes:
        if recipe["time"] <= max_time:
            found.append(f"{recipe['name']}, preparation time {recipe['time']} min")
    return found

"""
A function named search_by_ingredient(filename: str, ingredient: str), which takes a filename and a search string as its arguments. 
The function should go through the file and select all recipes whose ingredients contain the given search string.
The names of these recipes are returned in a list just like in the second part, with the preparation time appended.
"""

def search_by_ingredient(filename: str, ingredient: str):
    recipes = load_recipes(filename)
    found = []
    for recipe in recipes:
        if ingredient.lower() in (ing.lower() for ing in recipe["ingredients"]):
            found.append(f"{recipe['name']}, preparation time {recipe['time']} min")
    return found
