goal = 10000
steps = 0

while True:
    line = input()
    if line == 'Going home':
        home_steps = int(input())
        steps += home_steps
        if steps >= goal:
            print('Goal reached! Good job!')
            print(f'{steps - goal} steps over the goal!')
        else:
            print(f'{goal - steps} more steps to reach goal.')
        break

    steps += int(line)
    if steps >= goal:
        print('Goal reached! Good job!')
        print(f'{steps - goal} steps over the goal!')
        break
