def create_person_description(first_name: str, last_name: str, age: int, town_name: str) -> str:
    """
    Creates a sentence with information about a person.

    Args:
        first_name: the person's first name
        last_name: the person's last name
        age: the person's age
        town_name: the town where the person is from

    Returns:
        A formatted description string
    """
    if not first_name.strip() or not last_name.strip() or age < 0 or not town_name.strip():
        return 'Invalid input.'
    return f'You are {first_name} {last_name}, a {age}-years old person from {town_name}.'


if __name__ == '__main__':
    input_first_name: str = input()
    input_last_name: str = input()
    input_age: int = int(input())
    input_town: str = input()

    message: str = create_person_description(
        first_name=input_first_name,
        last_name=input_last_name,
        age=input_age,
        town_name=input_town
    )

    print(message)
