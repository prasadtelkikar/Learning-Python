import textwrap
def wrap(string, max_width):
    #textwrap.wrap(string, max_width) this will return string in list format by slicing list into words of at most length max_width
    return textwrap.fill(string, max_width) # same as wrap(), but will return string not list

string, max_width = input(), int(input())
result = wrap(string, max_width)
print(result)
    