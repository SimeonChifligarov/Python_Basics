goal = 10000
steps = 0
line = input()

while line != 'Going home':
    steps += int(line)
    if steps >= goal:
        print('Goal reached! Good job!')
        print(f'{steps - goal} steps over the goal!')
        break

    line = input()
else:
    home_steps = int(input())
    steps += home_steps

    if steps >= goal:
        print('Goal reached! Good job!')
        print(f'{steps - goal} steps over the goal!')
    else:
        print(f'{goal - steps} more steps to reach goal.')
