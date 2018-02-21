# code is not working properly failing 4 test cases passing only 2
def Capitalize(string):
    for word in string.split():
        print(word)

    #list = [word[0].upper() + word[1:] for word in string.split()]
    #capitalizedString = ' '.join(list)
    return capitalizedString

string = input()
capitalizeString  = Capitalize(string)
print(capitalizeString)
