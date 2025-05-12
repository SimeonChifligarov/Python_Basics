width = int(input())
length = int(input())

total = width * length
used = 0
line = input()

while line != 'STOP':
    used += int(line)
    if used > total:
        print(f'No more cake left! You need {used - total} pieces more.')
        break

    line = input()
else:
    print(f'{total - used} pieces are left.')
