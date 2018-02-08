menu_special = {
    "breakfast" : "sausage and egg",
    "lunch" : "split pea soup and garlic bread",
   "dinner" : "2 hot dogs and onion rice"
   }

print(menu_special.keys())
print(menu_special.values())

print(menu_special.__contains__("breakfast"))   #True : breakfast is present in menu_special dictionary
print(menu_special.__contains__("Breakfast"))   #False : Breakfast is not available in dictionary as it is case sensitive
