def authenticate_user() -> None:
    """
    Asks for a username and password, then repeatedly asks for a password until the correct one is entered.

    Args:
        None

    Returns:
        None
    """
    username: str = input()
    correct_password: str = input()
    entered_password: str = input()

    while entered_password != correct_password:
        entered_password = input()

    print(f'Welcome {username}!')


if __name__ == '__main__':
    authenticate_user()
