def is_special_number(dividend, number):
    digits = [int(digit) for digit in str(number)]
    return all(digit != 0 and dividend % digit == 0 for digit in digits)


n = int(input())
special_numbers = []

for num in range(1_111, 10_000):
    if is_special_number(n, num):
        special_numbers.append(str(num))

print(' '.join(special_numbers))
