def process_deposits_loop() -> None:
    """
    Keeps reading deposit amounts and updates total. Ends on 'NoMoreMoney' or invalid deposit.

    Returns:
        None
    """
    total_balance: float = 0.0

    while True:
        entry: str = input()

        if entry == 'NoMoreMoney':
            break

        try:
            amount: float = float(entry)
        except ValueError:
            return

        if amount < 0:
            print('Invalid operation!')
            break

        print(f'Increase: {amount:.2f}')
        total_balance += amount

    print(f'Total: {total_balance:.2f}')


if __name__ == '__main__':
    process_deposits_loop()
