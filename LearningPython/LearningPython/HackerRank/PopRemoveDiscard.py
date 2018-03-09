n = int(input())
s = set(map(int, input().split())) 

length = int(input())
i =0
while(i < length):
  inp = input().split()
  if(inp[0] == 'pop'):
    s.pop()
  elif(inp[0] == 'remove'):
    s.remove(int(inp[1]))
  elif(inp[0] == 'discard'):
    s.discard(int(inp[1]))
  i = i + 1
  
result = 0

for s1 in s:
  result = result + s1
  
print(result)
