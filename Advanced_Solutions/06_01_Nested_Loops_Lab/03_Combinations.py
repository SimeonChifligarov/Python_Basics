def count_valid_combinations(target_sum: int) -> int:
    """
    Counts how many combinations of natural numbers (including 0) satisfy x1 + x2 + x3 = target_sum.

    Args:
        target_sum: an integer number

    Returns:
        Number of valid combinations
    """
    if target_sum < 0:
        return 0

    valid_count = 0

    for value_1 in range(target_sum + 1):
        for value_2 in range(target_sum + 1):
            value_3 = target_sum - value_1 - value_2
            if 0 <= value_3 <= target_sum:
                valid_count += 1

    return valid_count


if __name__ == '__main__':
    target_input: int = int(input())
    result: int = count_valid_combinations(target_sum=target_input)
    print(result)
