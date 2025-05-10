def calculate_ski_holiday_price(stay_days: int, room_type: str, feedback: str) -> float:
    """
    Calculates the total price for a ski holiday stay based on room type, duration, and feedback.

    Args:
        stay_days: Number of days Atanas will stay (nights = days - 1).
        room_type: Type of room chosen.
        feedback: 'positive' or 'negative' feedback after the stay.

    Returns:
        The total price after all discounts and feedback adjustment.
    """
    if stay_days <= 1:
        return 0.0

    nights: int = stay_days - 1

    price_per_night: dict[str, float] = {
        'room for one person': 18.0,
        'apartment': 25.0,
        'president apartment': 35.0,
    }

    base_price: float = nights * price_per_night.get(room_type, 0.0)

    if room_type == 'apartment':
        if stay_days < 10:
            base_price *= 0.7
        elif 10 <= stay_days <= 15:
            base_price *= 0.65
        else:
            base_price *= 0.5
    elif room_type == 'president apartment':
        if stay_days < 10:
            base_price *= 0.9
        elif 10 <= stay_days <= 15:
            base_price *= 0.85
        else:
            base_price *= 0.8

    if feedback == 'positive':
        base_price *= 1.25
    elif feedback == 'negative':
        base_price *= 0.9

    return base_price


if __name__ == '__main__':
    days_input: int = int(input())
    room_input: str = input()
    review_input: str = input()

    total_cost: float = calculate_ski_holiday_price(
        stay_days=days_input,
        room_type=room_input,
        feedback=review_input
    )
    print(f'{total_cost:.2f}')
