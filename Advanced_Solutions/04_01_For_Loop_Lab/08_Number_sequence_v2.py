import sys


def find_min_and_max(count: int) -> tuple[int, int]:
    """
    Finds the smallest and biggest numbers from a given number of user inputs.

    Args:
        count: how many numbers to read

    Returns:
        A tuple of (max, min) values
    """
    if count <= 0:
        return 0, 0

    max_value: int = -sys.maxsize
    min_value: int = sys.maxsize

    for _ in range(count):
        current_number: int = int(input())
        if current_number > max_value:
            max_value = current_number
        if current_number < min_value:
            min_value = current_number

    return max_value, min_value


if __name__ == '__main__':
    numbers_count: int = int(input())
    max_number, min_number = find_min_and_max(count=numbers_count)
    print(f'Max number: {max_number}')
    print(f'Min number: {min_number}')
