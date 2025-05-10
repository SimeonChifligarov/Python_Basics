def suggest_outfit(degree_value: int, time_of_day: str) -> str:
    """
    Suggests what clothes and shoes to wear based on temperature and time of day.

    Args:
        degree_value: The outside temperature in degrees.
        time_of_day: Time of day - 'Morning', 'Afternoon', or 'Evening'.

    Returns:
        A sentence recommending outfit and shoes.
    """
    if time_of_day not in {'Morning', 'Afternoon', 'Evening'}:
        return 'Invalid time of day.'

    if degree_value < 10:
        return 'Temperature too low for suggestion.'

    outfit: str = ''
    shoes: str = ''

    if 10 <= degree_value <= 18:
        if time_of_day == 'Morning':
            outfit, shoes = 'Sweatshirt', 'Sneakers'
        else:
            outfit, shoes = 'Shirt', 'Moccasins'
    elif 18 < degree_value <= 24:
        if time_of_day == 'Afternoon':
            outfit, shoes = 'T-Shirt', 'Sandals'
        else:
            outfit, shoes = 'Shirt', 'Moccasins'
    elif degree_value >= 25:
        if time_of_day == 'Morning':
            outfit, shoes = 'T-Shirt', 'Sandals'
        elif time_of_day == 'Afternoon':
            outfit, shoes = 'Swim Suit', 'Barefoot'
        else:
            outfit, shoes = 'Shirt', 'Moccasins'

    return f"It's {degree_value} degrees, get your {outfit} and {shoes}."


if __name__ == '__main__':
    temperature_input: int = int(input())
    period_input: str = input()

    recommendation: str = suggest_outfit(
        degree_value=temperature_input,
        time_of_day=period_input
    )
    print(recommendation)
