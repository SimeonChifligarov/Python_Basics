import sys

min_number = sys.maxsize
value = input()

while value != 'Stop':
    current = int(value)
    if current < min_number:
        min_number = current

    value = input()

print(min_number)
