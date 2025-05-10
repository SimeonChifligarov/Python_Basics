hour_input = int(input())
day_input = input()

if 10 <= hour_input <= 18 and day_input in ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']:
    status = 'open'
else:
    status = 'closed'

print(status)
