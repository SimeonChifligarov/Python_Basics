def sum_until_target() -> None:
    """
    Reads numbers until their total becomes greater than or equal to a target number.

    Returns:
        None
    """
    target_sum: int = int(input())
    current_sum: int = 0

    while current_sum < target_sum:
        number: int = int(input())
        current_sum += number

    print(current_sum)


if __name__ == '__main__':
    sum_until_target()
