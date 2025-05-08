def greet_person_by_name_message(person_name: str) -> str:
    """
    Makes a greeting message using the given name.

    Args:
        person_name: the name of the person

    Returns:
        A greeting string with the person's name
    """
    if not person_name.strip():
        return 'Hello, !'
    return f'Hello, {person_name}!'


if __name__ == '__main__':
    input_name: str = input()
    greeting_message: str = greet_person_by_name_message(person_name=input_name)
    print(greeting_message)
