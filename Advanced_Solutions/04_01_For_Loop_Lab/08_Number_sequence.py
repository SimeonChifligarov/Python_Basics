def find_min_and_max(count: int) -> tuple[int, int]:
    """
    Finds the minimum and maximum values among a sequence of integers.

    Args:
        count: the number of integers to read

    Returns:
        A tuple with the maximum and minimum values
    """
    if count <= 0:
        return 0, 0

    first_number: int = int(input())
    current_max: int = first_number
    current_min: int = first_number

    for _ in range(count - 1):
        current_number: int = int(input())
        if current_number > current_max:
            current_max = current_number
        if current_number < current_min:
            current_min = current_number

    return current_max, current_min


if __name__ == '__main__':
    total_numbers: int = int(input())
    max_value, min_value = find_min_and_max(count=total_numbers)
    print(f'Max number: {max_value}')
    print(f'Min number: {min_value}')
