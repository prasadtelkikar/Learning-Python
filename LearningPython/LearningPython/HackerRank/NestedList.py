#Reference https://medium.com/@nick3499/python-nested-list-comprehensions-7462b4e21626
#Reference~1 https://stackoverflow.com/questions/15181867/understanding-the-set-function

n = int(input())
# New way to read two inputs for iterating n times
nList = [[input(), float(input())] for _ in range(n)]

#Set function removes duplicate numbers in list then convert it into list and then sort it.
#Store second lowest element
second_lowest = sorted(list(set([marks for name, marks in nList])))[1]

#Variable to store result
result = []
length = len(nList)
i = 0
#Extract all elements having same lowest marks
while(i < length):
    if(nList[i][1] == second_lowest):
        result.append(nList[i][0])
    i = i + 1

#again sort list for output
result.sort()
#print result
for i in result:
    print(i)