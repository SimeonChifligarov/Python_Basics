def is_prime(value: int) -> bool:
    """
    Checks if a number is a prime.

    Args:
        value: The number to check.

    Returns:
        True if number is prime, otherwise False.
    """
    if value < 2:
        return False

    for divider in range(2, int(value ** 0.5) + 1):
        if value % divider == 0:
            return False

    return True


def classify_numbers() -> None:
    """
    Reads numbers until 'stop' is entered.
    Calculates and prints the sum of prime and non-prime numbers.
    """
    sum_primes: int = 0
    sum_non_primes: int = 0

    while True:
        entry: str = input()
        if entry == 'stop':
            break

        try:
            number: int = int(entry)
        except ValueError:
            continue

        if number < 0:
            print('Number is negative.')
            continue

        if is_prime(value=number):
            sum_primes += number
        else:
            sum_non_primes += number

    print(f'Sum of all prime numbers is: {sum_primes}')
    print(f'Sum of all non prime numbers is: {sum_non_primes}')


if __name__ == '__main__':
    classify_numbers()
