day_input = input()

price = 0
if day_input == 'Monday' or day_input == 'Tuesday' or day_input == 'Friday':
    price = 12
elif day_input == 'Wednesday' or day_input == 'Thursday':
    price = 14
elif day_input == 'Saturday' or day_input == 'Sunday':
    price = 16

print(price)
