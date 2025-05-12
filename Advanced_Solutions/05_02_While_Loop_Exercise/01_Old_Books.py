def find_favorite_book(favorite_book: str) -> None:
    """
    This function helps Ani find her favorite book.
    It checks every book title one by one until the book is found
    or the books are over.

    Args:
        favorite_book: the book Ani is searching for

    Returns:
        Nothing. It prints the result directly.
    """
    current_title: str = input()
    checked_count: int = 0

    while current_title != 'No More Books':
        if current_title == favorite_book:
            print(f'You checked {checked_count} books and found it.')
            return

        checked_count += 1
        current_title = input()

    print('The book you search is not here!')
    print(f'You checked {checked_count} books.')


if __name__ == '__main__':
    favorite_book_input: str = input()
    find_favorite_book(favorite_book=favorite_book_input)
