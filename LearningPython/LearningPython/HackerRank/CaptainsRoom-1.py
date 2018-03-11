n = int(input())
lis = list(map(int, input().split()))
set1 = set(lis)
sumSet = 0
sumList = sum(lis) 
#Super awesome python
for i in set1:
    sumSet = sumSet + (i * n)

diff = sumSet - sumList
result = diff // (n - 1)

print(result)