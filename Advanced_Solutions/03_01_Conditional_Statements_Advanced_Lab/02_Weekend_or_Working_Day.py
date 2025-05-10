def classify_day(day_name: str) -> str:
    """
    Tells if the given day is a working day, weekend or invalid.

    Args:
        day_name: Name of the day in English.

    Returns:
        A string - 'Working day', 'Weekend' or 'Error'.
    """
    working_days: set[str] = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', }
    weekend_days: set[str] = {'Saturday', 'Sunday', }

    if day_name in working_days:
        return 'Working day'

    if day_name in weekend_days:
        return 'Weekend'

    return 'Error'


if __name__ == '__main__':
    user_day: str = input()
    result = classify_day(day_name=user_day)
    print(result)
