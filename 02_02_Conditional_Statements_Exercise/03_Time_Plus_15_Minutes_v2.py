hour = int(input())
minute = int(input())

total_minutes = hour * 60 + minute + 15
new_hour = (total_minutes // 60) % 24
new_minute = total_minutes % 60

print(f'{new_hour}:{new_minute:02d}')
