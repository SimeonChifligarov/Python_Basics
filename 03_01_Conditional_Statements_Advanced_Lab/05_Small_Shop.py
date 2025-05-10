product_input = input()
city_input = input()
quantity_input = float(input())

price = 0
if city_input == 'Sofia':
    if product_input == 'coffee':
        price = 0.50
    elif product_input == 'water':
        price = 0.80
    elif product_input == 'beer':
        price = 1.20
    elif product_input == 'sweets':
        price = 1.45
    elif product_input == 'peanuts':
        price = 1.60

elif city_input == 'Plovdiv':
    if product_input == 'coffee':
        price = 0.40
    elif product_input == 'water':
        price = 0.70
    elif product_input == 'beer':
        price = 1.15
    elif product_input == 'sweets':
        price = 1.30
    elif product_input == 'peanuts':
        price = 1.50

elif city_input == 'Varna':
    if product_input == 'coffee':
        price = 0.45
    elif product_input == 'water':
        price = 0.70
    elif product_input == 'beer':
        price = 1.10
    elif product_input == 'sweets':
        price = 1.35
    elif product_input == 'peanuts':
        price = 1.55

total_price = quantity_input * price
print(total_price)
