def is_valid_number(value: int) -> bool:
    """
    Checks if the number is valid (in range [100, 200] or equal to 0).

    Args:
        value: The number to be checked.

    Returns:
        True if valid, False otherwise.
    """
    return value == 0 or 100 <= value <= 200


if __name__ == '__main__':
    user_input: int = int(input())
    is_valid: bool = is_valid_number(value=user_input)
    if not is_valid:
        print('invalid')
