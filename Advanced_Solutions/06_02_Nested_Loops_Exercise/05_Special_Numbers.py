def is_special(number: int, divisor: int) -> bool:
    """
    Checks if all digits of the number divide the divisor without remainder.

    Args:
        number: The 4-digit number to check.
        divisor: The number to be divisible by each digit.

    Returns:
        True if all digits divide the divisor, False otherwise.
    """
    for digit_char in str(number):
        digit: int = int(digit_char)
        if digit == 0 or divisor % digit != 0:
            return False
    return True


def generate_special_numbers(limit: int) -> None:
    """
    Prints all 4-digit numbers from 1111 to 9999 that are 'special' with respect to the given limit.

    Args:
        limit: The number that must be divisible by all digits of the 4-digit number.
    """
    if limit < 1:
        return

    results: list[str] = [
        str(candidate)
        for candidate in range(1_111, 10_000)
        if is_special(number=candidate, divisor=limit)
    ]

    if results:
        print(' '.join(results))


if __name__ == '__main__':
    input_number: int = int(input())
    generate_special_numbers(limit=input_number)
