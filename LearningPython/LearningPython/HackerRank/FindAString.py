def count_substring(string, sub_string):
  countOcc = 0
  for i in (range(0, len(string) - len(sub_string) + 1)):
    flag = False
    for j in (range(0, len(sub_string))):
      if(string[i + j] != sub_string[j]):
        flag = False
        break
      else:
        flag = True
      
    if(flag):
      countOcc = countOcc + 1
    
  return countOcc


string = input().strip()
sub_string = input().strip()
count = count_substring(string, sub_string)
print(count)
