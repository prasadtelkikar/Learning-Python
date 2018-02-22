#Cheated by looking into discussion board
N, M = map(int,input().split()) # More than 6 lines of code will result in 0 score. Blank lines are not counted.
#Need to learn how for loop works
for i in range(1,N,2): 
    print((i * ".|.").center(M, '-'))
    
print("WELCOME".center(M, '-'))

#Need to learn how for loop works
for i in range(N-2,-1,-2): 
    print((i * ".|.").center(M, '-'))

