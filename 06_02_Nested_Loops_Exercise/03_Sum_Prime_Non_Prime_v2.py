def is_prime(n):
    if n < 2:
        return False
    for d in range(2, int(n ** 0.5) + 1):
        if n % d == 0:
            return False
    return True


prime_sum = 0
nonprime_sum = 0

while True:
    value = input()
    if value == 'stop':
        break

    number = int(value)
    if number < 0:
        print('Number is negative.')
        continue

    if is_prime(number):
        prime_sum += number
    else:
        nonprime_sum += number

print(f'Sum of all prime numbers is: {prime_sum}')
print(f'Sum of all non prime numbers is: {nonprime_sum}')
