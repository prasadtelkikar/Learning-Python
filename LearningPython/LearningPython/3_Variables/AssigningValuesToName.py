#https://stackoverflow.com/questions/26938799/printing-variables-in-python-3-4
first_string = "This is a string"
second_string = "This is another string"
first_number = 4
second_number = 5

#using format specifier
print("The variables are %s, %s, %d, %d" %(first_string, second_string, first_number, second_number))

#for python 3.x newer version: prefer str.format function ~ PREFER BELOW OVER FORMAT SPECIFIER
print("The variables are {}, {}, {}, {}".format(first_string, second_string, first_number, second_number))

