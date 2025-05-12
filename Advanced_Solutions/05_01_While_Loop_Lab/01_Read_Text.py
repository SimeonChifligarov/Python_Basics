def read_and_print_words() -> None:
    """
    Reads and prints words until the word 'Stop' is entered.

    Args:
        None

    Returns:
        None
    """
    word: str = input()
    while word != 'Stop':
        print(word)
        word = input()


if __name__ == '__main__':
    read_and_print_words()
