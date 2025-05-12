import sys


def find_min_number_loop() -> None:
    """
    Keeps reading integers and prints the smallest when 'Stop' is entered.

    Returns:
        None
    """
    min_value: int = sys.maxsize

    while True:
        input_value: str = input()
        if input_value == 'Stop':
            break

        current_number: int = int(input_value)
        if current_number < min_value:
            min_value = current_number

    print(min_value)


if __name__ == '__main__':
    find_min_number_loop()
