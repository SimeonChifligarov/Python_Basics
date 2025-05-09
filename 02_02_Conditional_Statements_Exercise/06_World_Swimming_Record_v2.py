from math import floor

record = float(input())
distance = float(input())
time_per_meter = float(input())

base_time = distance * time_per_meter
delay_count = floor(distance / 15)
total_time = base_time + delay_count * 12.5
difference = abs(record - total_time)

if total_time < record:
    print(f'Yes, he succeeded! The new world record is {total_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {difference:.2f} seconds slower.')
