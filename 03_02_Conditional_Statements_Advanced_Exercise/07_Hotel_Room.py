month = input()
nights = int(input())

studio_price = 0.0
apartment_price = 0.0

if month == 'May' or month == 'October':
    studio_price = 50.0
    apartment_price = 65.0
    if nights > 14:
        studio_price *= 0.7
    elif nights > 7:
        studio_price *= 0.95
elif month == 'June' or month == 'September':
    studio_price = 75.2
    apartment_price = 68.7
    if nights > 14:
        studio_price *= 0.8
elif month == 'July' or month == 'August':
    studio_price = 76.0
    apartment_price = 77.0

if nights > 14:
    apartment_price *= 0.9

studio_total = nights * studio_price
apartment_total = nights * apartment_price

print(f'Apartment: {apartment_total:.2f} lv.')
print(f'Studio: {studio_total:.2f} lv.')
