def calculate_fruit_price(fruit_name: str, day_name: str, amount: float) -> str:
    """
    Calculates the total price for a given fruit and quantity depending on the day.

    Args:
        fruit_name: Name of the fruit.
        day_name: Day of the week.
        amount: Quantity of fruit.

    Returns:
        A string with the total price formatted to 2 decimals or 'error' if invalid input.
    """
    weekday_prices: dict[str, float] = {
        'banana': 2.50,
        'apple': 1.20,
        'orange': 0.85,
        'grapefruit': 1.45,
        'kiwi': 2.70,
        'pineapple': 5.50,
        'grapes': 3.85,
    }

    weekend_prices: dict[str, float] = {
        'banana': 2.70,
        'apple': 1.25,
        'orange': 0.90,
        'grapefruit': 1.60,
        'kiwi': 3.00,
        'pineapple': 5.60,
        'grapes': 4.20,
    }

    weekdays: set[str] = {'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'}
    weekends: set[str] = {'Saturday', 'Sunday'}

    if day_name in weekdays:
        price_list = weekday_prices
    elif day_name in weekends:
        price_list = weekend_prices
    else:
        return 'error'

    if fruit_name not in price_list:
        return 'error'

    total = price_list[fruit_name] * amount
    return f'{total:.2f}'


if __name__ == '__main__':
    input_fruit: str = input()
    input_day: str = input()
    input_quantity: float = float(input())

    result: str = calculate_fruit_price(
        fruit_name=input_fruit,
        day_name=input_day,
        amount=input_quantity
    )

    print(result)
