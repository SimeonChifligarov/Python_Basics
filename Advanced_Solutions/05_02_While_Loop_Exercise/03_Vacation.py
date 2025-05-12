def track_savings(goal_amount: float, current_amount: float) -> None:
    """
    This function helps Jessie check if she can save enough money for a trip.
    She either spends or saves money each day, and the program stops when she saves enough,
    or when she spends money for 5 days in a row.

    Args:
        goal_amount: how much money she needs
        current_amount: how much money she has at the start

    Returns:
        Nothing. It prints the result directly.
    """
    saved_money: float = current_amount
    days_passed: int = 0
    consecutive_spend_days: int = 0

    while saved_money < goal_amount and consecutive_spend_days < 5:
        action: str = input()
        amount: float = float(input())
        days_passed += 1

        if action == 'spend':
            spent: float = min(saved_money, amount)
            saved_money -= spent
            consecutive_spend_days += 1
        elif action == 'save':
            saved_money += amount
            consecutive_spend_days = 0

    if consecutive_spend_days == 5:
        print('You can\'t save the money.')
        print(days_passed)
    else:
        print(f'You saved the money for {days_passed} days.')


if __name__ == '__main__':
    needed_money_input: float = float(input())
    available_money_input: float = float(input())
    track_savings(goal_amount=needed_money_input, current_amount=available_money_input)
