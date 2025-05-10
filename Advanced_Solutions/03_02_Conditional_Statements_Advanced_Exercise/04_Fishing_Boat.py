def is_fishing_trip_affordable(group_budget: int, season_name: str, fisherman_count: int) -> str:
    """
    Calculates if the fishing trip is affordable based on the season and group size.

    Args:
        group_budget: Total budget available.
        season_name: The current season - 'Spring', 'Summer', 'Autumn', or 'Winter'.
        fisherman_count: Number of fishermen in the group.

    Returns:
        A message indicating if the group can afford the trip and how much money is left or needed.
    """
    season_prices: dict[str, float] = {
        'Spring': 3000.0,
        'Summer': 4200.0,
        'Autumn': 4200.0,
        'Winter': 2600.0
    }

    base_price: float = season_prices.get(season_name, 0.0)

    if fisherman_count <= 6:
        base_price *= 0.9
    elif 7 <= fisherman_count <= 11:
        base_price *= 0.85
    else:
        base_price *= 0.75

    if fisherman_count % 2 == 0 and season_name != 'Autumn':
        base_price *= 0.95

    if group_budget >= base_price:
        remaining_money: float = group_budget - base_price
        return f'Yes! You have {remaining_money:.2f} leva left.'
    else:
        money_needed: float = base_price - group_budget
        return f'Not enough money! You need {money_needed:.2f} leva.'


if __name__ == '__main__':
    budget_input: int = int(input())
    season_input: str = input()
    fishermen_input: int = int(input())

    result: str = is_fishing_trip_affordable(
        group_budget=budget_input,
        season_name=season_input,
        fisherman_count=fishermen_input
    )
    print(result)
