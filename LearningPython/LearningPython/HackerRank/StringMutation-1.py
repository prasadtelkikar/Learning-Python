def StringMutation(string, position, char):
    strList = list(string)
    strList[position] = char
    string = ''.join(strList)
    return string

str = input()
position, newChar = input().split()
newString = StringMutation(str, int(position), newChar)
print(newString)
