days = int(input())
room = input()
review = input()

nights = days - 1
price = 0.0

if room == 'room for one person':
    price = nights * 18.0
elif room == 'apartment':
    price = nights * 25.0
    if days < 10:
        price *= 0.7
    elif days <= 15:
        price *= 0.65
    else:
        price *= 0.5
elif room == 'president apartment':
    price = nights * 35.0
    if days < 10:
        price *= 0.9
    elif days <= 15:
        price *= 0.85
    else:
        price *= 0.8

if review == 'positive':
    price *= 1.25
elif review == 'negative':
    price *= 0.9

print(f'{price:.2f}')
