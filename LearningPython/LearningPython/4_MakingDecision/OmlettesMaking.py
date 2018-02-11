omlettes_ordered = 5
omlettes_delivered = 0
fridge_contents = {"egg":8, "mushroom": 20, "pepper": 3, "cheese":2, "tomatto":4, "milk":13}
omlet_ingredients = {"egg":2, "mushroom":5, "pepper":1, "cheese":1, "milk":1}

while(omlettes_delivered < omlettes_ordered) :
    break_out = False
    for key, value in omlet_ingredients.items() :
      ingredient_needed = value
      print("Adding {} {} to the mix".format(value, key))
      fridge_contents[key] = fridge_contents[key] - ingredient_needed
      if(fridge_contents[key] < 0):
          print("There is not enough {} for another omlet".format(omlettes_ordered - omlettes_delivered))
          break_out = True

    omlettes_delivered += 1
    print("One more omlet made! {} more to go".format(omlettes_ordered - omlettes_delivered))
    
    #TODO: Defect not able to figure out what the error is. Logical error
    if(break_out == True):
        print("Out of ingredients, go shopping if you want to make more omelets")
        break
