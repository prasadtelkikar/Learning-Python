#function for addition
def do_plus(firstNumber, secondNumber):
    """Addition of two number and save result to sum variable"""
    sum = firstNumber + secondNumber
    return sum

#Function for substraction
def do_substraction(firstNumber, secondNumber):
    """Substraction of two numbers and save result to sub variable"""
    sub = 0
    if(firstNumber > secondNumber):
        sub = firstNumber - secondNumber
    else:
        sub = secondNumber - firstNumber
    return sub

#Function for Multiplication 
def do_multiplication(firstNumber, secondNumber):
    mul = firstNumber * secondNumber
    return mul

#Function for division
def do_division(firstNumber, secondNumber):
    try:
        div = firstNumber / secondNumber
        return div
    except ZeroDivisionError:
        return "Error due to divide by zero"


print("Addition of 3 and 4 is {}".format(do_plus(3, 4)))
print("Substraction of 3 and 4 is {}".format(do_substraction(3, 4)))
print("Substraction of 4 and 3 is {}".format(do_substraction(4, 3)))
print("Multiplication of 4 and 3 is {}".format(do_multiplication(4, 3)))
print("Division of 4 and 3 is {0:.gu2f}".format(do_division(4, 3)))
print("Division of 4 and 0 is {}".format(do_division(4, 0)))
