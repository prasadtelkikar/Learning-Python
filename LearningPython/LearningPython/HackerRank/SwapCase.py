def swap_case(s):
    swappedCase = ""
    for s1 in s:
        if(s1.isupper() == True):
            swappedCase += s1.lower()
        elif(s1.islower() == True):
            swappedCase += s1.upper()
        else:
            swappedCase += s1
            
    return swappedCase

s = input()
result = swap_case(s)
print(result)