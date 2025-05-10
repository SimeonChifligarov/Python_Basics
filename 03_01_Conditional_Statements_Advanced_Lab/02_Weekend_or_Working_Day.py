day_input = input()

if day_input in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']:
    result = 'Working day'
# if day_input == 'Monday' or day_input == 'Tuesday' or day_input == 'Wednesday' or day_input == 'Thursday' or day_input == 'Friday':  # noqa E501
#     result = 'Working day'

elif day_input in ['Saturday', 'Sunday']:
    result = 'Weekend'
# elif day_input == 'Saturday' or day_input == 'Sunday':
#     result = 'Weekend'

else:
    result = 'Error'

print(result)
