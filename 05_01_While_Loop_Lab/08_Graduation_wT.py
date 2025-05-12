name = input()
grade = 1
total = 0.0
fails = 0

while True:
    score = float(input())
    if score < 4.0:
        fails += 1
        if fails > 1:
            break

        continue

    total += score
    grade += 1
    if grade > 12:
        break

if fails <= 1:
    average = total / 12
    print(f'{name} graduated. Average grade: {average:.2f}')
else:
    print(f'{name} has been excluded at {grade} grade')
