def average(arr):
    distinctList = set(arr)
    length = len(distinctList)
    result = sum(distinctList) / length
    return result

n = int(input())
arr = list(map(int, input().split()))
result = average(arr)
print(result)
