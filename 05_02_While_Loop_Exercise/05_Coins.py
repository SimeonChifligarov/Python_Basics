change = float(input())
coins = 0
money = round(change * 100)

while money > 0:
    if money >= 200:
        money -= 200
    elif money >= 100:
        money -= 100
    elif money >= 50:
        money -= 50
    elif money >= 20:
        money -= 20
    elif money >= 10:
        money -= 10
    elif money >= 5:
        money -= 5
    elif money >= 2:
        money -= 2
    else:
        money -= 1
    coins += 1

print(coins)
