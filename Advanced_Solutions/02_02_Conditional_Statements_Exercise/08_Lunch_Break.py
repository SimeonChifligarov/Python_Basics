from math import ceil


def can_watch_episode(
        series_name: str,
        episode_duration: int,
        break_duration: int
) -> str:
    """
    This checks if there is enough break time to watch a full episode after lunch and rest.

    Args:
        series_name: Name of the TV series.
        episode_duration: Duration of the episode in minutes.
        break_duration: Total break time available in minutes.

    Returns:
        A message stating if there's enough time to watch the episode and how much time is left or needed.
    """
    lunch_time: float = break_duration / 8
    rest_time: float = break_duration / 4
    remaining_time: float = break_duration - lunch_time - rest_time
    time_difference: float = remaining_time - episode_duration

    if time_difference >= 0:
        return f'You have enough time to watch {series_name} and left with {ceil(time_difference)} minutes free time.'
    return f"You don't have enough time to watch {series_name}, you need {ceil(abs(time_difference))} more minutes."


if __name__ == '__main__':
    show_name: str = input()
    duration: int = int(input())
    break_time: int = int(input())

    result: str = can_watch_episode(
        series_name=show_name,
        episode_duration=duration,
        break_duration=break_time
    )
    print(result)
