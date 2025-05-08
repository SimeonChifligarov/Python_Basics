def calculate_food_order_cost(chicken_count: int, fish_count: int, veg_count: int) -> float:
    """
    Calculates the total food order cost including dessert and delivery.

    Args:
        chicken_count: number of chicken menus
        fish_count: number of fish menus
        veg_count: number of vegetarian menus

    Returns:
        The total price of the order
    """
    price_chicken = 10.35
    price_fish = 12.4
    price_veg = 8.15
    delivery_fee = 2.5

    subtotal: float = chicken_count * price_chicken + fish_count * price_fish + veg_count * price_veg
    dessert_fee: float = subtotal * 0.2

    return subtotal + dessert_fee + delivery_fee


if __name__ == '__main__':
    input_chicken: int = int(input())
    input_fish: int = int(input())
    input_veg: int = int(input())

    total_price: float = calculate_food_order_cost(
        chicken_count=input_chicken,
        fish_count=input_fish,
        veg_count=input_veg
    )
    print(total_price)
