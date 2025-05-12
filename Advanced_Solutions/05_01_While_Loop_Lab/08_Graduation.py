def process_student_grades() -> None:
    """
    Reads a student's yearly grades and determines if they graduate or get excluded.

    Returns:
        None
    """
    student_name: str = input()
    current_grade: int = 1
    total_score: float = 0.0
    fail_count: int = 0

    grade_input: str = input()

    while current_grade <= 12:
        grade: float = float(grade_input)

        if grade < 4.0:
            fail_count += 1
            if fail_count > 1:
                print(f'{student_name} has been excluded at {current_grade} grade')
                return

            grade_input = input()
            continue

        total_score += grade
        current_grade += 1

        if current_grade > 12:
            break

        grade_input = input()

    average_score: float = total_score / 12
    print(f'{student_name} graduated. Average grade: {average_score:.2f}')


if __name__ == '__main__':
    process_student_grades()
