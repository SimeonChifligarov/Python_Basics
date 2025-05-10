def calculate_flower_purchase(flower_type: str, flower_count: int, budget: int) -> str:
    """
    Calculates if the flower purchase is within the budget and returns the result.

    Args:
        flower_type: Type of flower chosen.
        flower_count: Number of flowers to buy.
        budget: Available budget.

    Returns:
        Message indicating whether the purchase is affordable and how much money is left or needed.
    """
    price_map: dict[str, float] = {
        'Roses': 5.0,
        'Dahlias': 3.8,
        'Tulips': 2.8,
        'Narcissus': 3.0,
        'Gladiolus': 2.5
    }

    base_price: float = price_map.get(flower_type, 0.0)
    total_cost: float = flower_count * base_price

    if flower_type == 'Roses' and flower_count > 80:
        total_cost *= 0.9
    elif flower_type == 'Dahlias' and flower_count > 90:
        total_cost *= 0.85
    elif flower_type == 'Tulips' and flower_count > 80:
        total_cost *= 0.85
    elif flower_type == 'Narcissus' and flower_count < 120:
        total_cost *= 1.15
    elif flower_type == 'Gladiolus' and flower_count < 80:
        total_cost *= 1.2

    if budget >= total_cost:
        remaining: float = budget - total_cost
        return f"Hey, you have a great garden with {flower_count} {flower_type} and {remaining:.2f} leva left."
    else:
        needed: float = total_cost - budget
        return f"Not enough money, you need {needed:.2f} leva more."


if __name__ == '__main__':
    flower_kind_input: str = input()
    count_input: int = int(input())
    budget_input: int = int(input())

    result: str = calculate_flower_purchase(
        flower_type=flower_kind_input,
        flower_count=count_input,
        budget=budget_input
    )
    print(result)
