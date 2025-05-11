count = int(input())

total = 0
max_value = float('-inf')

for _ in range(count):
    current = int(input())
    total += current
    if current > max_value:
        max_value = current

rest_sum = total - max_value

if max_value == rest_sum:
    print('Yes')
    print(f'Sum = {max_value}')
else:
    difference = abs(max_value - rest_sum)
    print('No')
    print(f'Diff = {difference}')
