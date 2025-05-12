favorite_book = input()
count_checked = 0

while True:
    current = input()
    if current == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {count_checked} books.')
        break

    if current == favorite_book:
        print(f'You checked {count_checked} books and found it.')
        break

    count_checked += 1
