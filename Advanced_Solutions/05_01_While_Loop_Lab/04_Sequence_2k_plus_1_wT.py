def print_sequence_loop() -> None:
    """
    Prints all numbers from the 2k+1 sequence that are less than or equal to a given number.

    Returns:
        None
    """
    limit: int = int(input())
    current_value: int = 1

    while True:
        if current_value > limit:
            break

        print(current_value)
        current_value = current_value * 2 + 1


if __name__ == '__main__':
    print_sequence_loop()
