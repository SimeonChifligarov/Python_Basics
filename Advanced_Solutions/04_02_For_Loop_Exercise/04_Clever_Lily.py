def check_savings_to_buy_washing_machine(age: int, washer_price: float, toy_price: int) -> None:
    """
    Checks if Lily has saved enough money to buy a washing machine.

    Args:
        age: Lily's current age.
        washer_price: The price of the washing machine.
        toy_price: The price of one toy.

    Returns:
        Nothing. Prints the result.
    """
    money_saved: float = 0.0
    money_gift: int = 10
    toy_count: int = 0

    for birthday in range(1, age + 1):
        if birthday % 2 == 0:
            money_saved += money_gift - 1
            money_gift += 10
        else:
            toy_count += 1

    total_money: float = money_saved + (toy_count * toy_price)

    if total_money >= washer_price:
        print(f'Yes! {total_money - washer_price:.2f}')
    else:
        print(f'No! {washer_price - total_money:.2f}')


if __name__ == '__main__':
    current_age: int = int(input())
    washing_machine_cost: float = float(input())
    single_toy_price: int = int(input())

    check_savings_to_buy_washing_machine(
        age=current_age,
        washer_price=washing_machine_cost,
        toy_price=single_toy_price
    )
