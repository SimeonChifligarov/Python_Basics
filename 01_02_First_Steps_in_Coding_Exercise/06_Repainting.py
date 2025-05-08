nylon_value = int(input())
paint_value = int(input())
thinner_value = int(input())
hours_value = int(input())

nylon_cost = (nylon_value + 2) * 1.5
paint_cost = paint_value * 1.1 * 14.5
thinner_cost = thinner_value * 5.0
bag_cost = 0.4

materials_total = nylon_cost + paint_cost + thinner_cost + bag_cost
labor_total = materials_total * 0.3 * hours_value
total_sum = materials_total + labor_total

print(total_sum)
