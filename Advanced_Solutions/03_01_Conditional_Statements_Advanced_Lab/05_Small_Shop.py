def calculate_price(city_name: str, product_name: str, quantity: float) -> float:
    """
    Calculates the total price of a product in a given city.

    Args:
        city_name: The name of the city.
        product_name: The name of the product.
        quantity: The quantity of the product.

    Returns:
        The total cost as a float.
    """
    prices: dict[str, dict[str, float]] = {
        'Sofia': {
            'coffee': 0.50,
            'water': 0.80,
            'beer': 1.20,
            'sweets': 1.45,
            'peanuts': 1.60,
        },
        'Plovdiv': {
            'coffee': 0.40,
            'water': 0.70,
            'beer': 1.15,
            'sweets': 1.30,
            'peanuts': 1.50,
        },
        'Varna': {
            'coffee': 0.45,
            'water': 0.70,
            'beer': 1.10,
            'sweets': 1.35,
            'peanuts': 1.55,
        },
    }

    if city_name not in prices or product_name not in prices[city_name] or quantity < 0:
        return 0.0

    return prices[city_name][product_name] * quantity


if __name__ == '__main__':
    input_product: str = input()
    input_city: str = input()
    input_quantity: float = float(input())

    total: float = calculate_price(
        city_name=input_city,
        product_name=input_product,
        quantity=input_quantity
    )

    print(total)
