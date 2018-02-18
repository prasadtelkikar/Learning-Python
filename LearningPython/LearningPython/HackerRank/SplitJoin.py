def split_and_join(line):
    list = line.split(' ')
    result = "-".join(list)
    return result

line = input()
result = split_and_join(line)
print(result)
