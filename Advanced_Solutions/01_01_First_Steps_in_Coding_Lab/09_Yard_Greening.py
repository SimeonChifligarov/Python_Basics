def calculate_landscaping_cost(area_size: float) -> tuple[float, float]:
    """
    Calculates the final price and discount for landscaping based on area size.

    Args:
        area_size: the number of square meters to be landscaped

    Returns:
        A tuple with (final_price, discount)
    """
    if area_size < 0.0:
        return 0.0, 0.0

    price_per_m2: float = 7.61
    total_price: float = area_size * price_per_m2
    discount_value: float = total_price * 0.18
    final_cost: float = total_price - discount_value

    return final_cost, discount_value


if __name__ == '__main__':
    input_area: float = float(input())

    final_amount, discount_amount = calculate_landscaping_cost(area_size=input_area)

    print(f'The final price is: {final_amount} lv.')
    print(f'The discount is: {discount_amount} lv.')
