def sum_user_numbers(count: int) -> int:
    """
    Sums a given number of integers provided by the user.

    Args:
        count: the number of integers to read and sum

    Returns:
        The total sum of the input integers
    """
    # if count <= 0:
    #     return 0

    # total_sum: int = 0
    # for _ in range(count):
    #     current_number: int = int(input())
    #     total_sum += current_number

    # one-liner:
    total_sum: int = sum([int(input()) for _ in range(count)])

    return total_sum


if __name__ == '__main__':
    number_of_inputs: int = int(input())
    result_sum: int = sum_user_numbers(count=number_of_inputs)
    print(result_sum)
