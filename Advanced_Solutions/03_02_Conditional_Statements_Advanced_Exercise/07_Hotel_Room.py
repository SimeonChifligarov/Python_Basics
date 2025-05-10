def calculate_hotel_prices(month_name: str, night_count: int) -> tuple[float, float]:
    """
    Calculates the total price for studio and apartment based on month and number of nights.

    Args:
        month_name: Month of the stay.
        night_count: Number of nights the guest will stay.

    Returns:
        A tuple with the apartment total price and studio total price.
    """
    studio_price_per_night: float = 0.0
    apartment_price_per_night: float = 0.0

    if month_name in {'May', 'October'}:
        studio_price_per_night = 50.0
        apartment_price_per_night = 65.0
        if night_count > 14:
            studio_price_per_night *= 0.7
        elif night_count > 7:
            studio_price_per_night *= 0.95
    elif month_name in {'June', 'September'}:
        studio_price_per_night = 75.2
        apartment_price_per_night = 68.7
        if night_count > 14:
            studio_price_per_night *= 0.8
    elif month_name in {'July', 'August'}:
        studio_price_per_night = 76.0
        apartment_price_per_night = 77.0

    if night_count > 14:
        apartment_price_per_night *= 0.9

    apartment_total: float = night_count * apartment_price_per_night
    studio_total: float = night_count * studio_price_per_night

    return apartment_total, studio_total


if __name__ == '__main__':
    month_input: str = input()
    nights_input: int = int(input())

    apartment_cost, studio_cost = calculate_hotel_prices(
        month_name=month_input,
        night_count=nights_input
    )

    print(f'Apartment: {apartment_cost:.2f} lv.')
    print(f'Studio: {studio_cost:.2f} lv.')
