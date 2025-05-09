def check_password(password_input: str) -> None:
    """
    This checks if the given password matches the correct one.

    Args:
        password_input: The password entered by the user.

    Returns:
        None
    """
    correct_password: str = 's3cr3t!P@ssw0rd'
    print('Welcome' if password_input == correct_password else 'Wrong password!')


if __name__ == '__main__':
    user_password: str = input()
    check_password(password_input=user_password)
