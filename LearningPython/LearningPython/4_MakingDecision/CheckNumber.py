while(True) :
    print("Enter input value: ")
    value = int(input())
    if(value > 0 and value < 10):
        print("Yes! Value is in between 1 and 9")
    #print()
    print("Do you want to continue? Press Y/y to stop : ")
    toContinue = input()
    if(toContinue == 'Y' or toContinue == 'y'):
        break
    else:
        print("Continuing...")
        print()

