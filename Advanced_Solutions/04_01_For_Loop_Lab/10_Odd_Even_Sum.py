def compare_even_odd_position_sums(number_count: int) -> None:
    """
    Compares the sum of numbers at even and odd positions.

    Args:
        number_count: total number of integers to read

    Returns:
        None
    """
    if number_count <= 0:
        print('Yes')
        print('Sum = 0')
        return

    even_sum: int = 0
    odd_sum: int = 0

    for index in range(1, number_count + 1):
        current_number: int = int(input())
        if index % 2 == 0:
            even_sum += current_number
        else:
            odd_sum += current_number

    if even_sum == odd_sum:
        print('Yes')
        print(f'Sum = {even_sum}')
    else:
        difference: int = abs(even_sum - odd_sum)
        print('No')
        print(f'Diff = {difference}')


if __name__ == '__main__':
    input_count: int = int(input())
    compare_even_odd_position_sums(number_count=input_count)
