def calculate_renovation_cost(nylon_m2: int, paint_liters: int, thinner_liters: int, work_hours: int) -> float:
    """
    Calculates the total renovation cost including materials and labor.

    Args:
        nylon_m2: square meters of protective nylon needed
        paint_liters: liters of paint needed
        thinner_liters: liters of paint thinner
        work_hours: number of hours the workers will take

    Returns:
        The total cost of the renovation
    """
    price_nylon = 1.5
    price_paint = 14.5
    price_thinner = 5.0
    bag_cost = 0.4

    nylon_total: float = (nylon_m2 + 2) * price_nylon
    paint_total: float = (paint_liters * 1.1) * price_paint
    thinner_total: float = thinner_liters * price_thinner

    material_sum : float= nylon_total + paint_total + thinner_total + bag_cost
    labor_cost: float = material_sum * 0.3 * work_hours

    return material_sum + labor_cost


if __name__ == '__main__':
    input_nylon: int = int(input())
    input_paint: int = int(input())
    input_thinner: int = int(input())
    input_hours: int = int(input())

    total_expense: float = calculate_renovation_cost(
        nylon_m2=input_nylon,
        paint_liters=input_paint,
        thinner_liters=input_thinner,
        work_hours=input_hours
    )
    print(total_expense)
