def sum_until_target_loop() -> None:
    """
    Adds input numbers until reaching or exceeding the target value.

    Returns:
        None
    """
    target_sum: int = int(input())
    current_sum: int = 0

    while True:
        if current_sum >= target_sum:
            break
        number: int = int(input())
        current_sum += number

    print(current_sum)


if __name__ == '__main__':
    sum_until_target_loop()
