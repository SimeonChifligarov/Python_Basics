def print_characters_one_per_line(text_input: str) -> None:
    """
    Prints each character from the input text on a separate line.

    Args:
        text_input: the string whose characters will be printed

    Returns:
        None
    """
    # if not text_input:
    #     return

    # [print(character) for character in text_input]
    print('\n'.join(text_input))


if __name__ == '__main__':
    user_text: str = input()
    print_characters_one_per_line(text_input=user_text)
