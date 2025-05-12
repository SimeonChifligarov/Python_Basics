name = input()
grade = 1
total = 0.0
fails = 0
score = input()

while grade <= 12:
    mark = float(score)
    if mark < 4.0:
        fails += 1
        if fails > 1:
            break

        score = input()
        continue

    total += mark
    grade += 1
    if grade > 12:
        break

    score = input()

is_success = fails <= 1 and grade > 12
if is_success:
    average = total / 12
    print(f'{name} graduated. Average grade: {average:.2f}')
else:
    print(f'{name} has been excluded at {grade} grade')
