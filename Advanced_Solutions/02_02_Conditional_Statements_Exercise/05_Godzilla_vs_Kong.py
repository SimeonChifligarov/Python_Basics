def can_start_filming(
        budget: float,
        extras_count: int,
        costume_price: float
) -> str:
    """
    This checks if the movie budget is enough to cover set and costume expenses.

    Args:
        budget: Total available budget.
        extras_count: Number of extras.
        costume_price: Price for one costume.

    Returns:
        A message stating whether filming can start or how much money is missing.
    """
    set_cost: float = budget * 0.1
    total_costume_price: float = extras_count * costume_price

    if extras_count > 150:
        total_costume_price *= 0.9

    total_expense: float = set_cost + total_costume_price
    remaining: float = budget - total_expense

    if remaining < 0:
        return f'Not enough money!\nWingard needs {abs(remaining):.2f} leva more.'
    return f'Action!\nWingard starts filming with {remaining:.2f} leva left.'


if __name__ == '__main__':
    movie_budget: float = float(input())
    number_of_extras: int = int(input())
    single_costume_price: float = float(input())

    result: str = can_start_filming(
        budget=movie_budget,
        extras_count=number_of_extras,
        costume_price=single_costume_price
    )
    print(result)
