def MergeTheTools(string, value):
    """Iterate through string and spit by size of value and remove redundent letters from splitted string"""
    length = len(string)
    size = length / int(value)
    output = ""

    for i in range(0, length + 1):
        if(i != 0 and i % (int(value)) == 0):
            #Reference : https://stackoverflow.com/questions/9841303/removing-duplicate-characters-from-a-string
            print(''.join(sorted(set(output), key=output.index)))
            output = ""

        if(i == length):
            break

        output += string[i]

string = input()
value = input()
MergeTheTools(string, value)

