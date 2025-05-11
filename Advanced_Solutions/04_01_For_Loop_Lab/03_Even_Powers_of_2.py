def print_even_powers_of_two(limit_power: int) -> None:
    """
    Prints the even powers of 2 from 0 up to the given power.

    Args:
        limit_power: the highest power to compute 2 raised to

    Returns:
        None
    """
    # if limit_power < 0:
    #     return

    [print(2 ** power) for power in range(0, limit_power + 1, 2)]


if __name__ == '__main__':
    max_power: int = int(input())
    print_even_powers_of_two(limit_power=max_power)
