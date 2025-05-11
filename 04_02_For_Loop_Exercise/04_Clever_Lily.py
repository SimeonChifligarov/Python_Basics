age = int(input())
price_washer = float(input())
price_toy = int(input())

total_money = 0
gift_money = 10
toy_counter = 0

for year in range(1, age + 1):
    if year % 2 == 0:
        total_money += gift_money - 1
        gift_money += 10
    else:
        toy_counter += 1

total_money += toy_counter * price_toy

if total_money >= price_washer:
    print(f'Yes! {total_money - price_washer:.2f}')
else:
    print(f'No! {price_washer - total_money:.2f}')
