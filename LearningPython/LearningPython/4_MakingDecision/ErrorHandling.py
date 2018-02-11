fridge_contents = {"Egg":8, "mushroom":20, "pepper":3, "cheese":2, "tomato": 4, "milk":14}

try:
    for key, value in fridge_contents.items() :
        if(value > 3):
            print("Lets have some juice")
except KeyError:
    print("Aww, Need to get grocery from mall")

