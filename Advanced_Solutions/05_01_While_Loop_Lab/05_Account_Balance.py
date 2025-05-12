def process_deposits() -> None:
    """
    Reads deposit amounts and calculates total balance. Stops on 'NoMoreMoney' or invalid input.

    Returns:
        None
    """
    total_balance: float = 0.0
    entry: str = input()

    while entry != 'NoMoreMoney':
        try:
            amount: float = float(entry)
        except ValueError:
            return

        if amount < 0:
            print('Invalid operation!')
            break

        print(f'Increase: {amount:.2f}')
        total_balance += amount

        entry = input()

    print(f'Total: {total_balance:.2f}')


if __name__ == '__main__':
    process_deposits()
