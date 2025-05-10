def is_in_range_excluding_zero(value: int) -> bool:
    """
    Checks if the number is between -100 and 100 and not equal to zero.

    Args:
        value: An integer number.

    Returns:
        True if the number is in range and not zero, otherwise False.
    """
    # if value == 0:
    #     return False
    #
    # if value < -100 or value > 100:
    #     return False
    #
    # return True

    return -100 <= value <= 100 and value != 0


if __name__ == '__main__':
    user_number: int = int(input())
    is_valid: bool = is_in_range_excluding_zero(value=user_number)
    print('Yes' if is_valid else 'No')
