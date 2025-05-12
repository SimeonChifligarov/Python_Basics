import sys

max_number = -sys.maxsize
value = input()

while value != 'Stop':
    current = int(value)
    if current > max_number:
        max_number = current

    value = input()

print(max_number)
