def print_even_or_odd(number_value: int) -> None:
    """
    This tells if the number is even or odd.

    Args:
        number_value: The integer to check.

    Returns:
        None
    """
    print('even' if number_value % 2 == 0 else 'odd')


if __name__ == '__main__':
    user_input: int = int(input())
    print_even_or_odd(number_value=user_input)
