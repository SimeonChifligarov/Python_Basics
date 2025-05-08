def calculate_basketball_expenses(annual_fee: int) -> float:
    """
    Calculates the total cost for basketball equipment and training for one year.

    Args:
        annual_fee: the training fee for one year

    Returns:
        The total expenses including equipment
    """
    shoes_price: float = annual_fee * 0.6
    outfit_price: float = shoes_price * 0.8
    ball_price: float = outfit_price * 0.25
    accessories_price: float = ball_price * 0.2

    return annual_fee + shoes_price + outfit_price + ball_price + accessories_price


if __name__ == '__main__':
    input_fee: int = int(input())
    total_cost: float = calculate_basketball_expenses(annual_fee=input_fee)
    print(total_cost)
