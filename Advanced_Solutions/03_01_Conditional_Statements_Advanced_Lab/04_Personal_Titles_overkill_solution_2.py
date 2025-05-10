def get_title_by_age_and_gender(age_value: float, gender_value: str) -> str:
    """
    Returns a polite title based on age and gender.

    Args:
        age_value: A float number representing the age.
        gender_value: A string, either 'm' or 'f'.

    Returns:
        A string with a title like 'Mr.', 'Miss', etc., or 'Invalid input' if not applicable.
    """
    titles: dict[str, dict[bool, str]] = {
        'm': {
            True: 'Mr.',
            False: 'Master',
        },
        'f': {
            True: 'Ms.',
            False: 'Miss',
        }
    }

    if gender_value not in titles or age_value < 0:
        return 'Invalid input'

    is_adult: bool = age_value >= 16
    return titles[gender_value][is_adult]


if __name__ == '__main__':
    input_age: float = float(input())
    input_gender: str = input()
    result: str = get_title_by_age_and_gender(
        age_value=input_age,
        gender_value=input_gender
    )
    print(result)
