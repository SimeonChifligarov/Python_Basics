def print_bigger_number(first_number: int, second_number: int) -> None:
    """
    This prints the bigger number from two integers.

    Args:
        first_number: The first number entered.
        second_number: The second number entered.

    Returns:
        None
    """

    # print(max(first_number, second_number))
    print(first_number if first_number >= second_number else second_number)


if __name__ == '__main__':
    input_1: int = int(input())
    input_2: int = int(input())
    print_bigger_number(first_number=input_1, second_number=input_2)
