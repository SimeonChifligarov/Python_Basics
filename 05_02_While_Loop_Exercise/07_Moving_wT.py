w = int(input())
l = int(input())
h = int(input())

space = w * l * h
filled = 0

while True:
    line = input()
    if line == 'Done':
        print(f'{space - filled} Cubic meters left.')
        break

    filled += int(line)
    if filled > space:
        print(f'No more free space! You need {filled - space} Cubic meters more.')
        break
