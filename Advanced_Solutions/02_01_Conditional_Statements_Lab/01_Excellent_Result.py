def print_if_excellent(grade_input: float) -> None:
    """
    This prints 'Excellent!' if the grade is 5.50 or more.

    Args:
        grade_input: The number representing the grade.

    Returns:
        None
    """
    if grade_input < 5.5:
        return
    print('Excellent!')


if __name__ == '__main__':
    user_grade: float = float(input())
    print_if_excellent(grade_input=user_grade)
