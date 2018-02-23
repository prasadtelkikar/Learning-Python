# code is not working properly failing 4 test cases passing only 2
def capitalize(string):
  chars = list(string)
  chars[0] = chars[0].upper()
  for ch in range(1, len(string)):
    if(chars[ch] == ' '):
       chars[ch + 1] = chars[ch + 1].upper()
       
  temp = ''.join(chars)
  return temp

string = input()
capitalized_string = capitalize(string)
print(capitalized_string)