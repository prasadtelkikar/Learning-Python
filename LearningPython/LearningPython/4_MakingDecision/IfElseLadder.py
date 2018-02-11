milk_price = 1.5

#If else ladder
if (milk_price < 1.25) :
    print("Buy two cartons of milk, they are on sale")
elif (milk_price < 2.5) :
    print("Buy one carton of milk, there is normal price")
else :
    print("Go somewhere else ! Milk price is high here")


#Repetition : How to do something - again and again

omlet_ingredients = {"egg":2, "mushroom":5, "pepper":1, "cheese":1, "milk":1}

print(omlet_ingredients.keys())
ingredients = omlet_ingredients.keys()

for key, value in omlet_ingredients.items() :
    print("Adding {} {} to the mix".format(value, key))

#while(len(ingredients) > 0) :
 #   current_ingredient = ingredients.pop(0)
  #  print("Adding {} {} to the mix".format(omlet_ingredients[curent_ingredient], current_ingredient))
