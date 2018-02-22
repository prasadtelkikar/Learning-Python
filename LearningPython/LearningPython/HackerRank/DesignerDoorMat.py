#My faliure attempt and obivously first attempt
#https://www.hackerrank.com/challenges/designer-door-mat/forum/comments/418032

list = input().split()
n = int(list[0])
m = int(list[1])
firstHalf = int(n / 2)
secondHalf = firstHalf

str = ".|."
mainString = str

while(firstHalf > 0):
  print(mainString.center(m, '-'))
  mainString = mainString + str + str
  firstHalf = firstHalf - 1

print("WELCOME".center(m, '-'))

mainString = str * (n - 2)
while(secondHalf > 0):
  print(mainString.center(m, '-'))
  mainString = mainString.replace('.|.', '', 2)
  secondHalf = secondHalf - 1
