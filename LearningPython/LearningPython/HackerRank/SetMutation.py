n = int(input())
set1 = set(map(int, input().split()))
sum = 0
n1 = int(input())

while(n1 > 0):
    s = input().split()
    set2 = set(map(int, input().split()))
    if(s[0] == 'intersection_update'):
        set1.intersection_update(set2)
    elif(s[0] == 'update'):
        set1.update(set2)
    elif(s[0] == 'symmetric_difference_update'):
        set1.symmetric_difference_update(set2)
    elif(s[0] == 'difference_update'):
        set1.difference_update(set2)
    n1 = n1 - 1

for s1 in set1:
    sum = sum + s1

print(sum)