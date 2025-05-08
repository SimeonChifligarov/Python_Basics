pens_value = int(input())
markers_value = int(input())
cleaner_value = int(input())
discount_value = int(input())

total_cost = pens_value * 5.8 + markers_value * 7.2 + cleaner_value * 1.2
final_price = total_cost - (total_cost * discount_value / 100)

print(final_price)
