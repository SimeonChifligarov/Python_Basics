def is_office_open(hour: int, day: str) -> bool:
    """
    Checks if the office is open based on the provided hour and day.

    Args:
        hour: An integer representing the hour.
        day: A string representing the day of the week.

    Returns:
        True if the office is open, otherwise False.
    """
    working_days: set[str] = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'}

    return 10 <= hour <= 18 and day in working_days


if __name__ == '__main__':
    input_hour: int = int(input())
    input_day: str = input()
    is_open: bool = is_office_open(hour=input_hour, day=input_day)
    print('open' if is_open else 'closed')
