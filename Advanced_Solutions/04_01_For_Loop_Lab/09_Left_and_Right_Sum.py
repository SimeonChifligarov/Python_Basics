def compare_left_right_sums(pair_count: int) -> None:
    """
    Reads 2 * n integers, splits them into two halves, and compares their sums.

    Args:
        pair_count: the number of elements in each half

    Returns:
        None
    """
    if pair_count <= 0:
        print('Yes, sum = 0')
        return

    left_sum: int = 0
    right_sum: int = 0

    for index in range(pair_count * 2):
        current_value: int = int(input())
        if index < pair_count:
            left_sum += current_value
        else:
            right_sum += current_value

    if left_sum == right_sum:
        print(f'Yes, sum = {left_sum}')
    else:
        difference: int = abs(left_sum - right_sum)
        print(f'No, diff = {difference}')


if __name__ == '__main__':
    input_count: int = int(input())
    compare_left_right_sums(pair_count=input_count)
