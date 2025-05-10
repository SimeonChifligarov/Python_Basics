fruit_input = input()
day_input = input()
quantity_input = float(input())

price = 0
is_valid = True

if day_input in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    if fruit_input == 'banana':
        price = 2.50
    elif fruit_input == 'apple':
        price = 1.20
    elif fruit_input == 'orange':
        price = 0.85
    elif fruit_input == 'grapefruit':
        price = 1.45
    elif fruit_input == 'kiwi':
        price = 2.70
    elif fruit_input == 'pineapple':
        price = 5.50
    elif fruit_input == 'grapes':
        price = 3.85
    else:
        is_valid = False

elif day_input in ['Saturday', 'Sunday']:
    if fruit_input == 'banana':
        price = 2.70
    elif fruit_input == 'apple':
        price = 1.25
    elif fruit_input == 'orange':
        price = 0.90
    elif fruit_input == 'grapefruit':
        price = 1.60
    elif fruit_input == 'kiwi':
        price = 3.00
    elif fruit_input == 'pineapple':
        price = 5.60
    elif fruit_input == 'grapes':
        price = 4.20
    else:
        is_valid = False

else:
    is_valid = False

if is_valid:
    total_price = price * quantity_input
    print(f'{total_price:.2f}')
else:
    print('error')
