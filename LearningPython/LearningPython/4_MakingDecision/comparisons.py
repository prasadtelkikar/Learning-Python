print("1 == 1 : {}".format(1 == 1))
print("1 == 2 : {}".format(1 == 2))
print("1.23 == 1 : {}".format(1.23 == 1))
print("1.0 == 1 : {}".format(1.0 == 1))
print("5 < 3 : {}".format(5 < 3))
print("10 > 2 : {}".format(10 > 2))

a = "Mackintosh Apples"
b = "Blackbarry"
c = "Golden Delicious Apples"

print("Mackintosh Apples == Blackbarry: {}".format(a == b))
print("Mackintosh Apples == Blackbarry: {}".format(b == c))

print(a[-len("apples"):-1] == c[-len("apples"):-1])

apples = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
apple_tree = ["Golden Delicious", "Fuji", "Mitsu", "Mackintosh"]
print("apples == apple_tree : {}".format(apples == apple_tree))

apple_tree = ["Mackintosh", "Golden Delicious", "Fuji", "Mitsu"]
print("Updated apple_tree - apples == apple_tree : {}".format(apples == apple_tree))

print("Pumpkin == pumpkin: {}".format("Pumpkin == pumpkin"))
print("Pumpkin.lower() == pumpkin.lower() : {}".format("Pumpkin".lower() == "pumpkin".lower()))
