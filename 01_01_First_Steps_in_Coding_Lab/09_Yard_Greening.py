area_value = float(input())

price_total = area_value * 7.61
discount_applied = price_total * 0.18
final_total = price_total - discount_applied

print(f'The final price is: {final_total} lv.')
print(f'The discount is: {discount_applied} lv.')
