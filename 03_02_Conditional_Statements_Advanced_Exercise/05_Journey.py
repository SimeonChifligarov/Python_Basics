budget = float(input())
season = input()

destination = ''
accommodation = ''
spent = 0.0

if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        spent = budget * 0.3
        accommodation = 'Camp'
    else:
        spent = budget * 0.7
        accommodation = 'Hotel'
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        spent = budget * 0.4
        accommodation = 'Camp'
    else:
        spent = budget * 0.8
        accommodation = 'Hotel'
else:
    destination = 'Europe'
    spent = budget * 0.9
    accommodation = 'Hotel'

print(f'Somewhere in {destination}')
print(f'{accommodation} - {spent:.2f}')
