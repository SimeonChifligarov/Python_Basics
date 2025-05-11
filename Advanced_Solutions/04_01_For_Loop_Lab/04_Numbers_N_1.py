def print_reverse_from_number(start_number: int) -> None:
    """
    Prints numbers starting from a given number down to 1.

    Args:
        start_number: the number to start counting down from

    Returns:
        None
    """
    # if start_number <= 1:
    #     return

    [print(current) for current in range(start_number, 0, -1)]


if __name__ == '__main__':
    user_input: int = int(input())
    print_reverse_from_number(start_number=user_input)
