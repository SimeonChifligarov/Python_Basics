def print_numbers_in_range(start: int, end: int) -> None:
    """
    Prints numbers from a start to an end value, each on a new line.

    Args:
        start: the number to start printing from
        end: the number to end printing at

    Returns:
        None
    """
    # if start > end:
    #     return

    [print(current_number) for current_number in range(start, end + 1)]


if __name__ == '__main__':
    print_numbers_in_range(start=1, end=100)
