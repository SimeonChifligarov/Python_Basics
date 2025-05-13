def find_magic_sum_combination(start: int, end: int, magic_number: int) -> None:
    """
    Finds the first pair of numbers in the given range whose sum equals the magic number.

    Args:
        start: the start of the range (inclusive)
        end: the end of the range (inclusive)
        magic_number: the target sum to find

    Returns:
        None
    """
    if start > end:
        print('0 combinations - neither equals', magic_number)
        return

    combination_index = 0

    for number_1 in range(start, end + 1):
        for number_2 in range(start, end + 1):
            combination_index += 1
            if number_1 + number_2 == magic_number:
                print(f'Combination N:{combination_index} ({number_1} + {number_2} = {magic_number})')
                return

    print(f'{combination_index} combinations - neither equals {magic_number}')


if __name__ == '__main__':
    range_start: int = int(input())
    range_end: int = int(input())
    target_sum: int = int(input())

    find_magic_sum_combination(start=range_start, end=range_end, magic_number=target_sum)
