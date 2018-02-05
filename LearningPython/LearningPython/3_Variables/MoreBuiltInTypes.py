# More Built-in types : Tuples, List and dictionary

#++++++++++++++++++++++++Tuples+++++++++++++++++++++
#tuples: Basic data type, sequence of values. Can not modify once it declare
#You can recognize tuples when they are created, because they are surrounded by parantheses. ()
tuples = ("String", "is", "filled", "by", "a", "tuples")

print("A {} {} {} {} {} {}".format(tuples[0], tuples[1], tuples[2], tuples[3], tuples[4], tuples[5]))

a = ("first", "second", "third")
b = (a, "b's second element")

#dereferencing the values
print("b[1]: {}".format(b[1]))

print("b[0][0]: {}".format(b[0][0]))
print("b[0][1]: {}".format(b[0][1]))
print("b[0][2]: {}".format(b[0][2]))

#Use of len function to calculate length of tuple
print("Length of tuple a = {}".format(len(a)))


#++++++++++++++++++++++++++++++++++List++++++++++++++++++++++++
#List: diff is only Changeable sequence of data
#You can recognize list when they are created, because they are surrounded by square brackets

breakfast = ["coffee", "tea", "toast", "egg"]

print("At index 0 : {}.\nAt index 1 : {}. \nAt index 2 : {}.\nAt index 3 : {}.".format(breakfast[0],breakfast[1],breakfast[2],breakfast[3]))

breakfast[3] = "sprouts"

print("\nAt index 3 after modification: {}".format(breakfast[3]))

breakfast.append("biscuits")

print("\nAt index 4 after appending to list: {}".format(breakfast[4]))

#++++++++++++++++++++++++++Dictionary+++++++++++++++++++++++++++

#Dictionary is created using curly braces. Dictionary is a combination of key and value
menu_special = {}
menu_special["Breakfast"] = "eggs"
menu_special["Lunch"] = "Rice and sambar"
menu_special["Dinner"] = "Fruits"

#different way to define dictionary
menu_special_1 = {"breakfast" : "eggs", "lunch":"Rice and sambar", "Dinner" : "Fruits"}

print("\nBreakfast : {} \nLunch : {} \nDinner : {}".format(menu_special["Breakfast"], menu_special["Lunch"], menu_special["Dinner"]))
