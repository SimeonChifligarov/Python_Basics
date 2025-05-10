number_input = int(input())

is_valid = -100 <= number_input <= 100 and number_input != 0

if is_valid:
    result = 'Yes'
else:
    result = 'No'

print(result)
