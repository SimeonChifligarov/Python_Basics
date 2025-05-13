student = 0
standard = 0
kid = 0

while True:
    name = input()
    if name == 'Finish':
        break

    seats = int(input())
    sold = 0
    while sold < seats:
        ticket = input()
        if ticket == 'End':
            break

        if ticket == 'student':
            student += 1
        elif ticket == 'standard':
            standard += 1
        elif ticket == 'kid':
            kid += 1
        sold += 1

    percent_full = sold / seats * 100
    print(f'{name} - {percent_full:.2f}% full.')

total = student + standard + kid

student_percent = student / total * 100
standard_percent = standard / total * 100
kid_percent = kid / total * 100

print(f'Total tickets: {total}')
print(f'{student_percent:.2f}% student tickets.')
print(f'{standard_percent:.2f}% standard tickets.')
print(f'{kid_percent:.2f}% kids tickets.')
