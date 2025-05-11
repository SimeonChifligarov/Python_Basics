actor = input()
points = float(input())
n = int(input())

for _ in range(n):
    judge = input()
    score = float(input())
    points += (len(judge) * score) / 2
    if points > 1250.5:
        print(f'Congratulations, {actor} got a nominee for leading role with {points:.1f}!')
        break
else:
    needed = 1250.5 - points
    print(f'Sorry, {actor} you need {needed:.1f} more!')
