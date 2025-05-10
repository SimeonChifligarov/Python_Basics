exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_total = exam_hour * 60 + exam_minute
arrival_total = arrival_hour * 60 + arrival_minute
diff = arrival_total - exam_total

if diff > 0:
    print('Late')
    if diff < 60:
        print(f'{diff} minutes after the start')
    else:
        h = diff // 60
        m = diff % 60
        print(f'{h}:{m:02d} hours after the start')
elif diff >= -30:
    print('On time')
    if diff != 0:
        print(f'{abs(diff)} minutes before the start')
else:
    print('Early')
    if abs(diff) < 60:
        print(f'{abs(diff)} minutes before the start')
    else:
        h = abs(diff) // 60
        m = abs(diff) % 60
        print(f'{h}:{m:02d} hours before the start')
