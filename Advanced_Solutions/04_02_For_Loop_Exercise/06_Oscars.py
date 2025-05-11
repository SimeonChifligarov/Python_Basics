NOMINATION_THRESHOLD: float = 1250.5


def evaluate_actor_nomination(name: str, base_points: float, judges: list[tuple[str, float]]) -> None:
    """
    Calculates if an actor gets nominated based on scores from judges.

    Args:
        name: Name of the actor.
        base_points: Initial points from the academy.
        judges: List of tuples (judge_name, judge_score).

    Returns:
        Nothing. Prints whether the actor is nominated or how many more points are needed.
    """
    total_points: float = base_points

    for judge_name, judge_score in judges:
        earned: float = (len(judge_name) * judge_score) / 2
        total_points += earned

        if total_points > NOMINATION_THRESHOLD:
            print(f'Congratulations, {name} got a nominee for leading role with {total_points:.1f}!')
            return

    needed: float = NOMINATION_THRESHOLD - total_points
    print(f'Sorry, {name} you need {needed:.1f} more!')


if __name__ == '__main__':
    actor_name: str = input()
    initial_points: float = float(input())
    number_of_judges: int = int(input())

    judge_data: list[tuple[str, float]] = [
        (input(), float(input())) for _ in range(number_of_judges)
    ]

    evaluate_actor_nomination(
        name=actor_name,
        base_points=initial_points,
        judges=judge_data
    )
