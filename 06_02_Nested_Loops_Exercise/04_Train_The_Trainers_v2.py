jury_size = int(input())
total_sum = 0
total_count = 0

while True:
    name = input()

    if name == 'Finish':
        break

    score_sum = 0
    for _ in range(jury_size):
        score = float(input())
        score_sum += score

    average = score_sum / jury_size
    print(f'{name} - {average:.2f}.')

    total_sum += score_sum
    total_count += jury_size

if total_count > 0:
    final = total_sum / total_count
    print(f"Student's final assessment is {final:.2f}.")
