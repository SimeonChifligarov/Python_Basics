favorite_book = input()
count_checked = 0
title = input()

while title != 'No More Books':
    if title == favorite_book:
        print(f'You checked {count_checked} books and found it.')
        break

    count_checked += 1
    title = input()
else:
    print('The book you search is not here!')
    print(f'You checked {count_checked} books.')
