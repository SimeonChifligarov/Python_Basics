def calculate_commission(city_name: str, sales_volume: float) -> str:
    """
    Calculates the commission amount based on city and sales volume.

    Args:
        city_name: Name of the city.
        sales_volume: Amount of sales.

    Returns:
        A string with the commission formatted to 2 decimals, or 'error' if input is invalid.
    """
    commissions: dict[str, dict[str, float]] = {
        'Sofia': {
            'small': 0.05,
            'medium': 0.07,
            'large': 0.08,
            'extra_large': 0.12,
        },
        'Varna': {
            'small': 0.045,
            'medium': 0.075,
            'large': 0.10,
            'extra_large': 0.13,
        },
        'Plovdiv': {
            'small': 0.055,
            'medium': 0.08,
            'large': 0.12,
            'extra_large': 0.145,
        },
    }

    if city_name not in commissions or sales_volume < 0:
        return 'error'

    if sales_volume <= 500:
        tier: str = 'small'
    elif sales_volume <= 1000:
        tier: str = 'medium'
    elif sales_volume <= 10000:
        tier: str = 'large'
    else:
        tier: str = 'extra_large'

    rate: float = commissions[city_name][tier]
    total: float = sales_volume * rate
    return f'{total:.2f}'


if __name__ == '__main__':
    input_city: str = input()
    input_sales: float = float(input())

    result: str = calculate_commission(
        city_name=input_city,
        sales_volume=input_sales
    )

    print(result)
