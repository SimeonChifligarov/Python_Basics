total_balance = 0.0

while True:
    entry = input()
    if entry == 'NoMoreMoney':
        break

    amount = float(entry)
    if amount < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')
    total_balance += amount

print(f'Total: {total_balance:.2f}')
