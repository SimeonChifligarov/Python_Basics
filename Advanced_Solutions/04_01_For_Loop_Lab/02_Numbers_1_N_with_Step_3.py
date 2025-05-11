def print_every_third_number(limit: int) -> None:
    """
    Prints every 3rd number from 1 up to a given limit, skipping others.

    Args:
        limit: the number to count up to

    Returns:
        None
    """
    # if limit < 1:
    #     return

    [print(current_value) for current_value in range(1, limit + 1, 3)]


if __name__ == '__main__':
    user_limit: int = int(input())
    print_every_third_number(limit=user_limit)
