flower_type = input()
flower_count = int(input())
budget = int(input())

total = 0.0

if flower_type == 'Roses':
    price = 5.0
    total = flower_count * price
    if flower_count > 80:
        total *= 0.9
elif flower_type == 'Dahlias':
    price = 3.8
    total = flower_count * price
    if flower_count > 90:
        total *= 0.85
elif flower_type == 'Tulips':
    price = 2.8
    total = flower_count * price
    if flower_count > 80:
        total *= 0.85
elif flower_type == 'Narcissus':
    price = 3.0
    total = flower_count * price
    if flower_count < 120:
        total *= 1.15
elif flower_type == 'Gladiolus':
    price = 2.5
    total = flower_count * price
    if flower_count < 80:
        total *= 1.2

if budget >= total:
    remaining = budget - total
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {remaining:.2f} leva left.')
else:
    needed = total - budget
    print(f'Not enough money, you need {needed:.2f} leva more.')
