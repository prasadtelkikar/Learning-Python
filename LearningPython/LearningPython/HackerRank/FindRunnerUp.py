#n stands for number of elements
n = int(input())
#One line list space seperated
oneLineList = input()
#instance of sorted list
list = []

#Sort list by ' '
for i in oneLineList.split(' '):
    list.append(int(i))

#sort list using built in function and pass true to sort in descending order
list.sort(reverse = True)
#Get max as first element in descending ordered list
max = list[0]
result = 0
#Iterate through desc ordered list
for l in list:
    #condition to check runner up in list
    if(l < max):
        result = l
        break

#Print runner-up
print(result)