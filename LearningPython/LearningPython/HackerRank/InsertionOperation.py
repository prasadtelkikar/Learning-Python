n1 = int(input())
s1 = set(map(int, input().split()))

n2 = int(input())
s2 = set(map(int, input().split()))

s3 = s1.intersection(s2)
print(len(s3))