import sys


def find_min_number() -> None:
    """
    Reads integers until 'Stop' is entered and prints the smallest one.

    Returns:
        None
    """
    min_value: int = sys.maxsize
    input_value: str = input()

    while input_value != 'Stop':
        current_number: int = int(input_value)
        if current_number < min_value:
            min_value = current_number

        input_value = input()

    print(min_value)


if __name__ == '__main__':
    find_min_number()
