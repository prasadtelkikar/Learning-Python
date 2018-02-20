def StringMutation(string, position, char):
    #To get substring = string[startIndex, length]
    string = string[:position] + char + string[position+1:]
    return string

str = input()
position, newChar = input().split()
newString = StringMutation(str, int(position), newChar)
print(newString)