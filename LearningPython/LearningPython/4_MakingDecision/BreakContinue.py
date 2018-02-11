#Break is used to break the looping
print("Use of Break\n")
for food in ("Milk", "Sprouts", "Eggs") :
    if(food == "Eggs"):
        break
    else:
        print("Vegetarian! I can eat {}".format(food))

#Continue: To skip records
print("Use of Continue\n")
for food in ("Milk", "Chicken", "Sprouts", "Eggs") :
    if(food == "Chicken"):
        continue
    else:
        print("Yes! I can eat {}".format(food))
    


