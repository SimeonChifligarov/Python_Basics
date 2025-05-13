n = int(input())

for value in range(1_111, 10_000):
    valid = True
    for ch in str(value):
        digit = int(ch)

        if digit == 0 or n % digit != 0:
            valid = False
            break

    if valid:
        print(value, end=' ')
