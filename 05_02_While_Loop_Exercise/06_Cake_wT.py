width = int(input())
length = int(input())
total = width * length
used = 0

while True:
    line = input()
    if line == 'STOP':
        print(f'{total - used} pieces are left.')
        break

    used += int(line)
    if used > total:
        print(f'No more cake left! You need {used - total} pieces more.')
        break
