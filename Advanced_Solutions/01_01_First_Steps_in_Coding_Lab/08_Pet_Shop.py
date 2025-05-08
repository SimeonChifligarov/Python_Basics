def calculate_pet_food_cost(dog_packages: int, cat_packages: int) -> float:
    """
    Calculates total cost for dog and cat food.

    Args:
        dog_packages: number of dog food packages
        cat_packages: number of cat food packages

    Returns:
        Total cost in lev
    """
    if dog_packages < 0 or cat_packages < 0:
        return 0.0

    return dog_packages * 2.5 + cat_packages * 4.0


if __name__ == '__main__':
    input_dog_count: int = int(input())
    input_cat_count: int = int(input())

    total_price: float = calculate_pet_food_cost(
        dog_packages=input_dog_count,
        cat_packages=input_cat_count
    )

    print(f'{total_price} lv.')
