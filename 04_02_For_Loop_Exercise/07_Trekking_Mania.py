groups = int(input())

musala = montblanc = kilimanjaro = k2 = everest = 0
total = 0

for _ in range(groups):
    climbers = int(input())
    total += climbers
    if climbers <= 5:
        musala += climbers
    elif climbers <= 12:
        montblanc += climbers
    elif climbers <= 25:
        kilimanjaro += climbers
    elif climbers <= 40:
        k2 += climbers
    else:
        everest += climbers

percent_musala = musala / total
percent_montblanc = montblanc / total
percent_kilimanjaro = kilimanjaro / total
percent_k2 = k2 / total
percent_everest = everest / total

print(f'{percent_musala:.2%}')
print(f'{percent_montblanc:.2%}')
print(f'{percent_kilimanjaro:.2%}')
print(f'{percent_k2:.2%}')
print(f'{percent_everest:.2%}')
