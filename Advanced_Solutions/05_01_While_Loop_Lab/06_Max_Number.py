import sys


def find_max_number() -> None:
    """
    Reads integers until 'Stop' is entered and prints the largest one.

    Returns:
        None
    """
    max_value: int = -sys.maxsize
    input_value: str = input()

    while input_value != 'Stop':
        current_number: int = int(input_value)
        if current_number > max_value:
            max_value = current_number

        input_value = input()

    print(max_value)


if __name__ == '__main__':
    find_max_number()
