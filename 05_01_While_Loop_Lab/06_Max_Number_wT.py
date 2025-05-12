import sys

max_number = -sys.maxsize

while True:
    value = input()
    if value == 'Stop':
        break

    current = int(value)
    if current > max_number:
        max_number = current

print(max_number)
