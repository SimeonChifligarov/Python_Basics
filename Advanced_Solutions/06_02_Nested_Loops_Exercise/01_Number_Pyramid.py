def print_number_pyramid(max_number: int) -> None:
    """
    Prints a number pyramid where each row has one more number than the previous,
    stopping when the maximum number is reached.

    Args:
        max_number: The last number to include in the pyramid.
    """
    if max_number < 1:
        return

    current: int = 1
    row_length: int = 1

    while current <= max_number:
        row_numbers: list[str] = [
            str(current + i) for i in range(min(row_length, max_number - current + 1))
        ]

        print(' '.join(row_numbers))

        current += row_length
        row_length += 1


if __name__ == '__main__':
    user_input: int = int(input())
    print_number_pyramid(max_number=user_input)
