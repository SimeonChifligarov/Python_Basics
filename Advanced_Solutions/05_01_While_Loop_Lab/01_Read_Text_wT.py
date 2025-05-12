def read_and_print_words_loop() -> None:
    """
    Reads and prints words in an infinite loop until 'Stop' is entered.

    Args:
        None

    Returns:
        None
    """
    while True:
        word: str = input()
        if word == 'Stop':
            return

        print(word)


if __name__ == '__main__':
    read_and_print_words_loop()
