floors = int(input())
rooms = int(input())

for floor in range(floors, 0, -1):
    if floor == floors:
        prefix = 'L'
    elif floor % 2 == 0:
        prefix = 'O'
    else:
        prefix = 'A'

    for room in range(rooms):
        print(f'{prefix}{floor}{room}', end=' ')
    print()
