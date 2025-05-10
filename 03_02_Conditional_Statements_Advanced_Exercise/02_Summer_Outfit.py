temperature = int(input())
period = input()

outfit = ''
shoes = ''

if 10 <= temperature <= 18:
    if period == 'Morning':
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif 18 < temperature <= 24:
    if period == 'Afternoon':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'
elif temperature >= 25:
    if period == 'Morning':
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif period == 'Afternoon':
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
    else:
        outfit = 'Shirt'
        shoes = 'Moccasins'

print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
