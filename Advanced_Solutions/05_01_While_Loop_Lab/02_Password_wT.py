def authenticate_user_loop() -> None:
    """
    Repeatedly asks the user to enter the correct password until they succeed, then welcomes them.

    Args:
        None

    Returns:
        None
    """
    user_name: str = input()
    user_password: str = input()

    while True:
        current_input: str = input()
        if current_input == user_password:
            break

    print(f'Welcome {user_name}!')


if __name__ == '__main__':
    authenticate_user_loop()
