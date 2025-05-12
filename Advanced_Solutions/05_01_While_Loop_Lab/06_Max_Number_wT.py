import sys


def find_max_number_loop() -> None:
    """
    Keeps reading integers and prints the largest when 'Stop' is entered.

    Returns:
        None
    """
    max_value: int = -sys.maxsize

    while True:
        input_value: str = input()
        if input_value == 'Stop':
            break

        current_number: int = int(input_value)
        if current_number > max_value:
            max_value = current_number

    print(max_value)


if __name__ == '__main__':
    find_max_number_loop()
