n1 = int(input())
n2 = int(input())
op = input()

if op in ['/', '%'] and n2 == 0:
    print(f'Cannot divide {n1} by zero')
elif op == '+':
    result = n1 + n2
    parity = 'even' if result % 2 == 0 else 'odd'
    print(f'{n1} + {n2} = {result} - {parity}')
elif op == '-':
    result = n1 - n2
    parity = 'even' if result % 2 == 0 else 'odd'
    print(f'{n1} - {n2} = {result} - {parity}')
elif op == '*':
    result = n1 * n2
    parity = 'even' if result % 2 == 0 else 'odd'
    print(f'{n1} * {n2} = {result} - {parity}')
elif op == '/':
    result = n1 / n2
    print(f'{n1} / {n2} = {result:.2f}')
elif op == '%':
    result = n1 % n2
    print(f'{n1} % {n2} = {result}')
