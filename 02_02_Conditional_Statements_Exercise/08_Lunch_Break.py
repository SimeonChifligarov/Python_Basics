from math import ceil

series = input()
episode_length = int(input())
break_length = int(input())

lunch = break_length / 8
rest = break_length / 4
time_left = break_length - lunch - rest
difference = time_left - episode_length

if difference >= 0:
    print(f'You have enough time to watch {series} and left with {ceil(difference)} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {ceil(abs(difference))} more minutes.")
