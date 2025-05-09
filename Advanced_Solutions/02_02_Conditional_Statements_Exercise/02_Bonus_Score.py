def calculate_bonus_points(start_points: int) -> tuple[float, float]:
    """
    This calculates the bonus points and the total points based on given rules.

    Args:
        start_points: The original score before bonuses.

    Returns:
        A tuple with bonus points and total points (original + bonus).
    """
    if start_points <= 100:
        bonus: float = 5
    elif start_points <= 1000:
        bonus: float = start_points * 0.2
    else:
        bonus: float = start_points * 0.1

    if start_points % 2 == 0:
        bonus += 1
    elif start_points % 10 == 5:
        bonus += 2

    total: float = start_points + bonus
    return bonus, total


if __name__ == '__main__':
    base_score: int = int(input())
    bonus_result, total_result = calculate_bonus_points(start_points=base_score)
    print(bonus_result, total_result, sep='\n')
