#Any Alphanumeric
#Any alphabetical
#any digits
#any lower character
# any upper character

if __name__ == '__main__':
    s = input()
    alnum = False
    alpha = False
    digit = False
    lowerChar = False
    upperChar = False
    
    for i in range(0, len(s)):
      if(s[i].isalpha()):
        alnum = True
        alpha = True
        if(not lowerChar):
          lowerChar = s[i].islower()
        if(not upperChar):
          upperChar = s[i].isupper()
      elif(s[i].isdigit() and not digit):
        alnum = True
        digit = True
      if(alnum and alpha and digit and lowerChar and upperChar):
        break
      
    print(alnum)
    print(alpha)
    print(digit)
    print(lowerChar)
    print(upperChar)
