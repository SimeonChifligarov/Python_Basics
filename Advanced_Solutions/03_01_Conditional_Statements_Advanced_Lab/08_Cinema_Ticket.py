def get_ticket_price(day_of_week: str) -> int:
    """
    Returns the cinema ticket price based on the day of the week.

    Args:
        day_of_week: A string representing the day.

    Returns:
        An integer representing the ticket price.
    """
    prices: dict[str, int] = {
        'Monday': 12,
        'Tuesday': 12,
        'Wednesday': 14,
        'Thursday': 14,
        'Friday': 12,
        'Saturday': 16,
        'Sunday': 16
    }

    return prices.get(day_of_week, 0)


if __name__ == '__main__':
    input_day: str = input()
    ticket_price: int = get_ticket_price(day_of_week=input_day)
    print(ticket_price)
