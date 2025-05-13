def plan_travel() -> None:
    """
    Reads travel destinations and required budgets, simulates saving money until budget is met,
    and announces when Ani can travel. Stops when 'End' is input as destination.

    Returns:
        None
    """
    while True:
        destination: str = input()

        if destination == 'End':
            break

        try:
            required_budget: float = float(input())
        except ValueError:
            continue

        saved_amount: float = 0.0

        while saved_amount < required_budget:
            try:
                current_saving: float = float(input())
                saved_amount += current_saving
            except ValueError:
                continue

        print(f'Going to {destination}!')


if __name__ == '__main__':
    plan_travel()
