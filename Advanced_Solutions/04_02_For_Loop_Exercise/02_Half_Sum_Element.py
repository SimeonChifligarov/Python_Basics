def check_element_equal_to_sum_of_rest(count: int, values: list[int]) -> None:
    """
    Checks if any number is equal to the sum of all other numbers.

    Args:
        count: Total count of numbers.
        values: List of all the numbers.

    Returns:
        Nothing. Just prints the result.
    """
    if count == 0 or not values:
        print('No')
        print('Diff = 0')
        return

    total_sum: int = sum(values)
    max_value: int = max(values)
    rest_sum: int = total_sum - max_value

    if max_value == rest_sum:
        print('Yes')
        print(f'Sum = {max_value}')
    else:
        difference: int = abs(max_value - rest_sum)
        print('No')
        print(f'Diff = {difference}')


if __name__ == '__main__':
    number_count: int = int(input())
    input_numbers: list[int] = [int(input()) for _ in range(number_count)]
    check_element_equal_to_sum_of_rest(count=number_count, values=input_numbers)
