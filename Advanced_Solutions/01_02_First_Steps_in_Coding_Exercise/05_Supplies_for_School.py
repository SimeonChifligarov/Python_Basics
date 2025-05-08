def calculate_total_cost(pens_count: int, markers_count: int, cleaner_liters: int, discount_percent: int) -> float:
    """
    Calculates the total cost of school supplies after discount.

    Args:
        pens_count: number of pen packages
        markers_count: number of marker packages
        cleaner_liters: liters of board cleaner
        discount_percent: discount as an integer percent

    Returns:
        The total amount to be paid after applying the discount
    """
    price_pens = 5.8
    price_markers = 7.2
    price_cleaner = 1.2

    subtotal: float = pens_count * price_pens + markers_count * price_markers + cleaner_liters * price_cleaner
    discount_value: float = subtotal * (discount_percent / 100)

    return subtotal - discount_value


if __name__ == '__main__':
    input_pens: int = int(input())
    input_markers: int = int(input())
    input_cleaner: int = int(input())
    input_discount: int = int(input())

    final_cost: float = calculate_total_cost(
        pens_count=input_pens,
        markers_count=input_markers,
        cleaner_liters=input_cleaner,
        discount_percent=input_discount
    )
    print(final_cost)
