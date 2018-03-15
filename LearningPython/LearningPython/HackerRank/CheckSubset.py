n = int(input())
resultList = []
while(n > 0):
  size1 = int(input())
  set1 = set(map(int, input().split()))
  size2 = int(input())
  set2 = set(map(int, input().split()))
  b =  not bool(set1.difference(set2))
  resultList.append(b)
  n = n - 1
  
for bresult in resultList:
  print(bresult)
