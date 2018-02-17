n = int(input())
dict = {}

for _ in range(n):
    str =  input().split(' ')
    key = str[0]
    x = float(str[1])
    y = float(str[2])
    z = float(str[3])
    avg = (x + y + z) / 3.00
    dict[key] = avg
    
inputKey = input()

print("{0:.2f}".format(dict[inputKey]))