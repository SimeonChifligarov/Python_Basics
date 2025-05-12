goal = float(input())
money = float(input())
days = 0
spend_days = 0

while money < goal and spend_days < 5:
    action = input()
    amount = float(input())
    days += 1

    if action == 'spend':
        money -= amount
        if money < 0:
            money = 0
        spend_days += 1
    else:
        money += amount
        spend_days = 0

if spend_days == 5:
    print('You can\'t save the money.')
    print(days)
else:
    print(f'You saved the money for {days} days.')
