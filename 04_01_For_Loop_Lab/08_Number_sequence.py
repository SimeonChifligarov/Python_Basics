n = int(input())

max_value = float('-inf')
min_value = float('inf')

for _ in range(n):
    number = int(input())
    if number > max_value:
        max_value = number
    if number < min_value:
        min_value = number

print(f'Max number: {max_value}')
print(f'Min number: {min_value}')
