start = int(input())
end = int(input())
magic = int(input())

count = 0
found = False

for first in range(start, end + 1):
    for second in range(start, end + 1):
        count += 1
        if first + second == magic:
            print(f'Combination N:{count} ({first} + {second} = {magic})')
            found = True
            break

    if found:
        break

if not found:
    print(f'{count} combinations - neither equals {magic}')
