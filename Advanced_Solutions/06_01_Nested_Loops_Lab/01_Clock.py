def print_all_day_minutes() -> None:
    """
    Prints every minute of the day from 0:0 to 23:59.

    Returns:
        None
    """

    for current_hour in range(24):
        for current_minute in range(60):
            print(f'{current_hour}:{current_minute}')


if __name__ == '__main__':
    print_all_day_minutes()
