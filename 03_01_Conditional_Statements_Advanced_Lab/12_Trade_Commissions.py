city_input = input()
sales_input = float(input())

is_valid = True
commission = 0

if sales_input < 0:
    is_valid = False

elif city_input == 'Sofia':
    if 0 <= sales_input <= 500:
        commission = 0.05
    elif sales_input <= 1000:
        commission = 0.07
    elif sales_input <= 10000:
        commission = 0.08
    else:
        commission = 0.12

elif city_input == 'Varna':
    if 0 <= sales_input <= 500:
        commission = 0.045
    elif sales_input <= 1000:
        commission = 0.075
    elif sales_input <= 10000:
        commission = 0.10
    else:
        commission = 0.13

elif city_input == 'Plovdiv':
    if 0 <= sales_input <= 500:
        commission = 0.055
    elif sales_input <= 1000:
        commission = 0.08
    elif sales_input <= 10000:
        commission = 0.12
    else:
        commission = 0.145

else:
    is_valid = False

if is_valid:
    total = sales_input * commission
    print(f'{total:.2f}')
else:
    print('error')
