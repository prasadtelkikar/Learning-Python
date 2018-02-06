N = int(input())
output = []

#While loop for number of test cases
while(N > 0):
    #split input using space. Program contains almost all list operations
    inputs = input().split(" ")
    if(inputs[0] == "insert"):
        output.insert(int(inputs[1]), int(inputs[2]))
    elif (inputs[0] == "print"): 
        print(str(output))
    elif(inputs[0] == "remove"):
        output.remove(int(inputs[1]))
    elif(inputs[0] == "append"):
        output.append(int(inputs[1]))
    elif(inputs[0] == "sort"):
        output.sort()
    elif(inputs[0] == "pop"):
        output.pop()
    elif(inputs[0] == "reverse"):
        output.reverse()
    N -= 1