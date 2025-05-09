def can_afford_trip(
        trip_cost: float,
        count_puzzles: int,
        count_dolls: int,
        count_bears: int,
        count_minions: int,
        count_trucks: int
) -> str:
    """
    This calculates if the money from selling toys is enough to pay for a trip.

    Args:
        trip_cost: The total cost of the trip.
        count_puzzles: Number of puzzles ordered.
        count_dolls: Number of talking dolls ordered.
        count_bears: Number of teddy bears ordered.
        count_minions: Number of minions ordered.
        count_trucks: Number of trucks ordered.

    Returns:
        A message saying if there is enough money or how much is missing, formatted to 2 decimal places.
    """
    price_puzzle: float = 2.6
    price_doll: float = 3.0
    price_bear: float = 4.1
    price_minion: float = 8.2
    price_truck: float = 2.0

    total_toys: int = count_puzzles + count_dolls + count_bears + count_minions + count_trucks

    total_price: float = (
            count_puzzles * price_puzzle +
            count_dolls * price_doll +
            count_bears * price_bear +
            count_minions * price_minion +
            count_trucks * price_truck
    )

    if total_toys >= 50:  # Apply 25% discount if 50 or more toys are ordered
        total_price *= 0.75

    total_price *= 0.9  # Deduct 10% for rent

    difference: float = total_price - trip_cost

    if difference >= 0:
        return f'Yes! {difference:.2f} lv left.'
    return f'Not enough money! {abs(difference):.2f} lv needed.'


if __name__ == '__main__':
    excursion_cost: float = float(input())
    puzzles: int = int(input())
    dolls: int = int(input())
    bears: int = int(input())
    minions: int = int(input())
    trucks: int = int(input())

    result: str = can_afford_trip(
        trip_cost=excursion_cost,
        count_puzzles=puzzles,
        count_dolls=dolls,
        count_bears=bears,
        count_minions=minions,
        count_trucks=trucks
    )
    print(result)
