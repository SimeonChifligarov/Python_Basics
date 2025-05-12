def minimum_coins_to_return(change: float) -> None:
    """
    This function calculates the minimum number of coins needed
    to return a given amount of change.

    Args:
        change: the amount of money to return

    Returns:
        Nothing. Prints the number of coins.
    """
    change_cents: int = round(change * 100)
    coin_count: int = 0
    coin_values: list[int] = [200, 100, 50, 20, 10, 5, 2, 1]

    index: int = 0
    while True:
        if change_cents == 0:
            print(coin_count)
            return

        if change_cents >= coin_values[index]:
            change_cents -= coin_values[index]
            coin_count += 1
        else:
            index += 1


if __name__ == '__main__':
    change_input: float = float(input())
    minimum_coins_to_return(change=change_input)
