def calculate_tennis_ranking(tournament_count: int, starting_points: int, results: list[str]) -> None:
    """
    Calculates Grigor's final ranking points, average points per tournament,
    and win percentage based on his tournament results.

    Args:
        tournament_count: Number of tournaments played.
        starting_points: Points at the beginning of the season.
        results: List of results ("W", "F", "SF") for each tournament.

    Returns:
        Nothing. Prints the final points, average points, and win percentage.
    """
    result_points: dict[str, int] = {
        'W': 2000,
        'F': 1200,
        'SF': 720,
    }

    total_points: int = starting_points
    earned_points: int = 0
    wins: int = 0

    for result in results:
        if result in result_points:
            earned_points += result_points[result]
            if result == 'W':
                wins += 1

    total_points += earned_points
    average_points: int = earned_points // tournament_count
    win_ratio: float = wins / tournament_count

    print(f'Final points: {total_points}')
    print(f'Average points: {average_points}')
    print(f'{win_ratio:.2%}')


if __name__ == '__main__':
    number_of_tournaments: int = int(input())
    initial_ranking_points: int = int(input())
    tournament_results: list[str] = [input() for _ in range(number_of_tournaments)]

    calculate_tennis_ranking(
        tournament_count=number_of_tournaments,
        starting_points=initial_ranking_points,
        results=tournament_results
    )
