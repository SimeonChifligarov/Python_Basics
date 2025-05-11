tournaments = int(input())
start_points = int(input())

total_earned = 0
wins = 0

for _ in range(tournaments):
    result = input()
    if result == 'W':
        total_earned += 2000
        wins += 1
    elif result == 'F':
        total_earned += 1200
    elif result == 'SF':
        total_earned += 720

final_points = start_points + total_earned
average_points = total_earned // tournaments
win_percent = wins / tournaments

print(f'Final points: {final_points}')
print(f'Average points: {average_points}')
print(f'{win_percent:.2%}')
