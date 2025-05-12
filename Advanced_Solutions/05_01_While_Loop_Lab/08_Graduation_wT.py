def process_student_grades_loop() -> None:
    """
    Processes grades in a loop and prints graduation or exclusion message.

    Returns:
        None
    """
    student_name: str = input()
    current_grade: int = 1
    total_score: float = 0.0
    fail_count: int = 0

    while True:
        grade_input: str = input()
        grade: float = float(grade_input)

        if grade < 4.0:
            fail_count += 1
            if fail_count > 1:
                print(f'{student_name} has been excluded at {current_grade} grade')
                return

            continue

        total_score += grade
        current_grade += 1

        if current_grade > 12:
            break

    average_score: float = total_score / 12
    print(f'{student_name} graduated. Average grade: {average_score:.2f}')


if __name__ == '__main__':
    process_student_grades_loop()
