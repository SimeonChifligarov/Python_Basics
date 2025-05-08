chicken_value = int(input())
fish_value = int(input())
veg_value = int(input())

order_sum = chicken_value * 10.35 + fish_value * 12.4 + veg_value * 8.15
dessert_sum = order_sum * 0.2
final_total = order_sum + dessert_sum + 2.5

print(final_total)
