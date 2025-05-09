def format_total_time(time_1: int, time_2: int, time_3: int) -> str:
    """
    This calculates total time from three durations in seconds and formats it as minutes:seconds.

    Args:
        time_1: Time for the first competitor in seconds.
        time_2: Time for the second competitor in seconds.
        time_3: Time for the third competitor in seconds.

    Returns:
        A string showing the total time in the format 'minutes:seconds' with leading zero on seconds.
    """
    total_seconds: int = time_1 + time_2 + time_3
    minutes: int = total_seconds // 60
    seconds: int = total_seconds % 60

    return f'{minutes}:{seconds:02d}'


if __name__ == '__main__':
    input_1: int = int(input())
    input_2: int = int(input())
    input_3: int = int(input())
    result: str = format_total_time(time_1=input_1, time_2=input_2, time_3=input_3)
    print(result)
