max_value = int(input())
current = 1
row = 1

while current <= max_value:
    printed = 0
    while printed < row and current <= max_value:
        print(current, end=' ')
        current += 1
        printed += 1
    print()
    row += 1
