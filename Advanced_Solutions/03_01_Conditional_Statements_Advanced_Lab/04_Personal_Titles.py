def get_title(age_value: float, gender_value: str) -> str:
    """
    Returns a title based on age and gender.

    Args:
        age_value: The age as a float number.
        gender_value: The gender as a single character 'm' or 'f'.

    Returns:
        A string representing the title.
    """
    genders: set[str] = {'m', 'f'}

    if gender_value not in genders:
        return 'Invalid input'

    if age_value < 0:
        return 'Invalid input'

    if gender_value == 'm':
        if age_value >= 16:
            return 'Mr.'
        return 'Master'
    elif gender_value == 'f':
        if age_value >= 16:
            return 'Ms.'
        return 'Miss'


if __name__ == '__main__':
    input_age: float = float(input())
    input_gender: str = input()
    result: str = get_title(age_value=input_age, gender_value=input_gender)
    print(result)
