import sys

min_number = sys.maxsize

while True:
    value = input()
    if value == 'Stop':
        break

    current = int(value)
    if current < min_number:
        min_number = current

print(min_number)
