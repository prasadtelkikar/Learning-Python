value = input()
name = "prasad"

try:
    #Type conversion
    intValue = int(value)
    #is operator returns true/false 
    if(type(name) is str):
        print("Everything is fine")
except (ValueError, TypeError) as e:
    print("Execution is in exception block")

   
print(type(value))
print(type(name))