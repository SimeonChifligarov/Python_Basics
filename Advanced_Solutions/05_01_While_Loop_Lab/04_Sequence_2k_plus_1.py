def print_sequence() -> None:
    """
    Prints numbers in the sequence 1, 3, 7, 15, 31, ... until reaching or passing a given limit.

    Returns:
        None
    """
    limit: int = int(input())
    current_value: int = 1

    while current_value <= limit:
        print(current_value)
        current_value = current_value * 2 + 1


if __name__ == '__main__':
    print_sequence()
