projection_type = input()
rows = int(input())
columns = int(input())

if projection_type == 'Premiere':
    price = 12.0
elif projection_type == 'Normal':
    price = 7.5
elif projection_type == 'Discount':
    price = 5.0
else:
    price = 0.0

total_seats = rows * columns
total_revenue = total_seats * price

print(f'{total_revenue:.2f} leva')
