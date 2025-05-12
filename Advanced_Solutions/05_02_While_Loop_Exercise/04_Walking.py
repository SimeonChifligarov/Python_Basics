def track_steps() -> None:
    """
    This function helps Gabi track her steps throughout the day.
    If she reaches her step goal, it congratulates her.
    If she goes home early, it checks if she has met the goal or not.

    Returns:
        Nothing. Prints the outcome directly.
    """
    step_goal: int = 10000
    total_steps: int = 0

    command: str = input()

    while command != 'Going home':
        steps_walked: int = int(command)
        total_steps += steps_walked
        if total_steps >= step_goal:
            print('Goal reached! Good job!')
            print(f'{total_steps - step_goal} steps over the goal!')
            return

        command = input()

    steps_home: int = int(input())
    total_steps += steps_home
    if total_steps >= step_goal:
        print('Goal reached! Good job!')
        print(f'{total_steps - step_goal} steps over the goal!')
    else:
        print(f'{step_goal - total_steps} more steps to reach goal.')


if __name__ == '__main__':
    track_steps()
