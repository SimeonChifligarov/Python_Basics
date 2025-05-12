def monitor_exam_performance(max_poor_grades: int) -> None:
    """
    This function helps track Marin's exam task performance.
    It stops if Marin receives too many poor grades or if he is told to stop.

    Args:
        max_poor_grades: how many poor grades are allowed

    Returns:
        Nothing. It prints result messages based on the situation.
    """
    poor_grade_limit: int = max_poor_grades
    total_score: int = 0
    problem_count: int = 0
    poor_grades: int = 0
    last_task_name: str = ''

    task_name: str = input()

    while task_name != 'Enough':
        grade: int = int(input())
        total_score += grade
        problem_count += 1
        last_task_name = task_name

        if grade <= 4:
            poor_grades += 1
            if poor_grades >= poor_grade_limit:
                print(f'You need a break, {poor_grades} poor grades.')
                return

        task_name = input()

    average_score: float = total_score / problem_count if problem_count > 0 else 0.0
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {problem_count}')
    print(f'Last problem: {last_task_name}')


if __name__ == '__main__':
    poor_grade_limit_input: int = int(input())
    monitor_exam_performance(max_poor_grades=poor_grade_limit_input)
