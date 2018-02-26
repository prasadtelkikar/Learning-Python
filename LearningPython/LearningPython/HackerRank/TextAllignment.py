#Replace all ______ with rjust, ljust or center. 
#I just replaced rjust, ljust and center and did trial and error. NO LOGIC IMPLEMENTATION
#not passing all test cases but, if you add rjust, ljust and center in right sequence as given over here then all test cases will pass
# DO NOT COPY PASTE THIS PROGRAM TO ON HACKERRANK TARMINAL
thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    print((c*i).rjust(thickness-1)+c+(c*i).ljust(thickness-1))

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt~check range it need to be divided by 2 ie thickness + 1 / 2 not thickness
for i in range((thickness)):
    print((c*thickness*5).center(thickness*6))    

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))    

#Bottom Cone
for i in range(thickness):
    print(((c*(thickness-i-1)).rjust(thickness)+c+(c*(thickness-i-1)).ljust(thickness)).rjust(thickness*6))
