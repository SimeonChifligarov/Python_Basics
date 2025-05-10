budget = int(input())
season = input()
fishermen = int(input())

price = 0.0

if season == 'Spring':
    price = 3000.0
elif season == 'Summer' or season == 'Autumn':
    price = 4200.0
elif season == 'Winter':
    price = 2600.0

if fishermen <= 6:
    price *= 0.9
elif 7 <= fishermen <= 11:
    price *= 0.85
else:
    price *= 0.75

if fishermen % 2 == 0 and season != 'Autumn':
    price *= 0.95

if budget >= price:
    left = budget - price
    print(f'Yes! You have {left:.2f} leva left.')
else:
    needed = price - budget
    print(f'Not enough money! You need {needed:.2f} leva.')
