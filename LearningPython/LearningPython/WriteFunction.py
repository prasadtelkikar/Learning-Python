year = int(input())

def is_leap(year):
    """Check year is leap or not"""
    leap = False

    if(year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        leap = True

    return leap


print(is_leap(year))