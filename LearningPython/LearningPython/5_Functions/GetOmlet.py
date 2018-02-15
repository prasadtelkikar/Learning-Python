def Get_Omlet_Ingredients(omlet_name):
    """This contains a dictionary of omlet names that can be produced and their ingredients"""
    #Basic ingredients of Omlets are
    ingredients = {"egg":2, "milk":1}
    if omlet_name == 'cheese':
        ingredients["cheese"] = 2
    elif omlet_name == 'western':
        ingredients["jack_cheese"] = 2
        ingredients["ham"] = 1
        ingredients["paper"] = 2
        ingredients["onion"] = 1
    elif omlet_name == 'greek':
        ingredients["feta_cheese"] = 1
        ingredients["spinach"] = 2
    else:
        print("That's not on the menu, sorry!")
        return None
    return ingredients

def Make_Food(ingredients_needed,  food_name):
    """make_food(ingredients_needed, food_name) takes the ingredients from ingredients_needed and make food_name"""
    for ingredients in ingredients_needed.keys():
        print("Adding {} of {} to make a {} omlet".format(ingredients_needed[ingredients], ingredients, food_name))
    print("Made {}".format(food_name))
    return food_name
        
cheese_omlet_Type = Make_Food(Get_Omlet_Ingredients("cheese"), "cheese")
print()
Western_omlet_Type = Make_Food(Get_Omlet_Ingredients("western"), "western")
print()
print(Western_omlet_Type)

