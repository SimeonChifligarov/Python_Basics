def add_fifteen_minutes(current_hour: int, current_minute: int) -> str:
    """
    This adds 15 minutes to the given time and returns it in 'h:mm' format.

    Args:
        current_hour: The hour part of the time (0-23).
        current_minute: The minute part of the time (0-59).

    Returns:
        A formatted string of the new time after 15 minutes.
    """
    total_minutes: int = current_hour * 60 + current_minute + 15
    new_hour: int = (total_minutes // 60) % 24
    new_minute: int = total_minutes % 60

    return f'{new_hour}:{new_minute:02d}'


if __name__ == '__main__':
    hour_input: int = int(input())
    minute_input: int = int(input())
    result: str = add_fifteen_minutes(current_hour=hour_input, current_minute=minute_input)
    print(result)
