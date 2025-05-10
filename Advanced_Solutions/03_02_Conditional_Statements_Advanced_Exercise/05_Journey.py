def plan_vacation(travel_budget: float, travel_season: str) -> str:
    """
    Decides where the programmer will go and how much money will be spent based on the budget and season.

    Args:
        travel_budget: Total amount of money available for travel.
        travel_season: Season of travel - 'summer' or 'winter'.

    Returns:
        A string with destination and accommodation details.
    """
    # # give types in one place:
    # destination: str = ''
    # accommodation: str = ''
    # spent_amount: float = 0.0

    if travel_budget <= 100:
        destination = 'Bulgaria'
        if travel_season == 'summer':
            spent_amount = travel_budget * 0.3
            accommodation = 'Camp'
        else:
            spent_amount = travel_budget * 0.7
            accommodation = 'Hotel'
    elif travel_budget <= 1000:
        destination = 'Balkans'
        if travel_season == 'summer':
            spent_amount = travel_budget * 0.4
            accommodation = 'Camp'
        else:
            spent_amount = travel_budget * 0.8
            accommodation = 'Hotel'
    else:
        destination = 'Europe'
        spent_amount = travel_budget * 0.9
        accommodation = 'Hotel'

    return f'Somewhere in {destination}\n{accommodation} - {spent_amount:.2f}'


if __name__ == '__main__':
    budget_input: float = float(input())
    season_input: str = input()

    result: str = plan_vacation(
        travel_budget=budget_input,
        travel_season=season_input
    )
    print(result)
