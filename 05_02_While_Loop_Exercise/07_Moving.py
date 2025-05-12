w = int(input())
l = int(input())
h = int(input())

space = w * l * h
filled = 0
line = input()

while line != 'Done':
    filled += int(line)
    if filled > space:
        print(f'No more free space! You need {filled - space} Cubic meters more.')
        break

    line = input()
else:
    print(f'{space - filled} Cubic meters left.')
