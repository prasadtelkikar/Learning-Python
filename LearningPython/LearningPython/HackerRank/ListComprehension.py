x = int(input())
y = int(input())
z = int(input())
n = int(input())

list = []
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if((i + j + k) != n):
                innerList = []
                innerList.append(i)
                innerList.append(j)
                innerList.append(k)
                list.append(innerList)

print(list)

#One line solution instead of above nesting of loop ~ solution from discussion tab           
#print ([[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b + c != n ])