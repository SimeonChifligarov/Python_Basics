def has_equal_even_odd_position_sums(number: int) -> bool:
    """
    Checks if the sum of digits at even positions is equal to the sum of digits at odd positions.

    Args:
        number: A six-digit integer.

    Returns:
        True if the sums are equal, otherwise False.
    """
    digits: str = str(number)
    if len(digits) != 6:
        return False

    even_sum: int = 0
    odd_sum: int = 0

    for index in range(6):
        digit_value: int = int(digits[index])
        if (index + 1) % 2 == 0:
            even_sum += digit_value
        else:
            odd_sum += digit_value

    return even_sum == odd_sum


def print_matching_numbers(start: int, end: int) -> None:
    """
    Prints all numbers between start and end (inclusive) for which the sum of digits
    at even and odd positions are equal.

    Args:
        start: The lower bound of the range (inclusive).
        end: The upper bound of the range (inclusive).
    """
    if start < 100_000 or end > 999_999 or start >= end:
        return

    result: list[str] = [
        str(number)
        for number in range(start, end + 1)
        if has_equal_even_odd_position_sums(number=number)
    ]

    if result:
        print(' '.join(result))


if __name__ == '__main__':
    lower_bound: int = int(input())
    upper_bound: int = int(input())
    print_matching_numbers(start=lower_bound, end=upper_bound)
