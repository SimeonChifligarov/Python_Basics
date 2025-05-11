n = int(input())

p1 = p2 = p3 = p4 = p5 = 0

for _ in range(n):
    number = int(input())
    if number < 200:
        p1 += 1
    elif number < 400:
        p2 += 1
    elif number < 600:
        p3 += 1
    elif number < 800:
        p4 += 1
    else:
        p5 += 1

percent_1 = p1 / n
percent_2 = p2 / n
percent_3 = p3 / n
percent_4 = p4 / n
percent_5 = p5 / n

print(f'{percent_1:.2%}')
print(f'{percent_2:.2%}')
print(f'{percent_3:.2%}')
print(f'{percent_4:.2%}')
print(f'{percent_5:.2%}')
