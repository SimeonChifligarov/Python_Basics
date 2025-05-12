max_poor = int(input())
poor_count = 0
total_score = 0
tasks_done = 0
last_task = ''

while True:
    task = input()
    if task == 'Enough':
        average = total_score / tasks_done if tasks_done > 0 else 0
        print(f'Average score: {average:.2f}')
        print(f'Number of problems: {tasks_done}')
        print(f'Last problem: {last_task}')
        break

    grade = int(input())
    total_score += grade
    tasks_done += 1
    last_task = task
    if grade <= 4:
        poor_count += 1
        if poor_count >= max_poor:
            print(f'You need a break, {poor_count} poor grades.')
            break
