n = int(input())

first = int(input())
max_value = first
min_value = first

for _ in range(n - 1):
    number = int(input())
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')
