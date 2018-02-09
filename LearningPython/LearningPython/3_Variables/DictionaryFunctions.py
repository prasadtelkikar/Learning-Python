menu_special = {
    "breakfast" : "sausage and egg",
    "lunch" : "split pea soup and garlic bread",
   "dinner" : "2 hot dogs and onion rice"
   }

print(menu_special.keys())
print(menu_special.values())

print(menu_special.__contains__("breakfast"))   #True : breakfast is present in menu_special dictionary
print(menu_special.__contains__("Breakfast"))   #False : Breakfast is not available in dictionary as it is case sensitive

slice_this_tuple = ("The", "next", "time", "we", "meet", "drinks", "are", "on", "me")
sliced_tuples = slice_this_tuple[5:9]

slice_this_list = ["The", "next", "time", "we", "meet", "drinks", "are", "on", "me"]
sliced_list = slice_this_list[5:9]

living_room_tuple = ("rug", "table", "chair", "TV", "dustbin", "shelf")
apartment = []
apartment.append(living_room_tuple)  #This is considered as a tuple in list

print(sliced_tuples)
print(sliced_list)

print("Appended apartment")
print(apartment)

apartment = []
apartment.extend(living_room_tuple)     #This is considered as a cloning of tuples into the list
print(apartment)