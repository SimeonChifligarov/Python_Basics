total_balance = 0.0
entry = input()

while entry != 'NoMoreMoney':
    amount = float(entry)
    if amount < 0:
        print('Invalid operation!')
        break

    print(f'Increase: {amount:.2f}')

    total_balance += amount
    entry = input()

print(f'Total: {total_balance:.2f}')
