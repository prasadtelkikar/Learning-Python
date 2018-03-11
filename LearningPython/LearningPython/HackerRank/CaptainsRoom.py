#Without use of set
n = int(input())
s = map(int, input().split())
dict = {}
captain = 0
for i in s:
    if not i in dict:
        dict[i] = 1
    else:
        dict[i] += 1
for key, value in dict.items(): 
    if(value == 1):
        captain = key
        break

print(captain)