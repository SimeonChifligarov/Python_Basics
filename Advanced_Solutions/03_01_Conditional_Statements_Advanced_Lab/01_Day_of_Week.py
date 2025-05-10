def get_weekday(day_index: int) -> str:
    """
    Returns the weekday name for a number between 1 and 7.
    Returns 'Error' if the number is not valid.

    Args:
        day_index: An integer from 1 to 7 representing a day.

    Returns:
        A string with the name of the day or 'Error'.
    """
    weekday_map: dict[int, str] = {
        1: 'Monday',
        2: 'Tuesday',
        3: 'Wednesday',
        4: 'Thursday',
        5: 'Friday',
        6: 'Saturday',
        7: 'Sunday',
    }

    return weekday_map.get(day_index, 'Error')


if __name__ == '__main__':
    user_number: int = int(input())
    output = get_weekday(day_index=user_number)
    print(output)
