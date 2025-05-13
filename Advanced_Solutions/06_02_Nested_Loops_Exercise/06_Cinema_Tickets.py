def process_movie_tickets() -> None:
    """
    Reads movie names, available seats, and ticket types from input.
    Calculates and prints the fill percentage for each movie and statistics for all tickets sold.
    """
    student_count: int = 0
    standard_count: int = 0
    kid_count: int = 0

    while True:
        movie_title: str = input()
        if movie_title == 'Finish':
            break

        free_seats: int = int(input())
        sold_tickets: int = 0

        while sold_tickets < free_seats:
            ticket_type: str = input()
            if ticket_type == 'End':
                break

            if ticket_type == 'student':
                student_count += 1
            elif ticket_type == 'standard':
                standard_count += 1
            elif ticket_type == 'kid':
                kid_count += 1

            sold_tickets += 1

        fill_percentage: float = (sold_tickets / free_seats) * 100
        print(f'{movie_title} - {fill_percentage:.2f}% full.')

    total_tickets = student_count + standard_count + kid_count

    if total_tickets == 0:
        return

    student_percent: float = (student_count / total_tickets) * 100
    standard_percent: float = (standard_count / total_tickets) * 100
    kid_percent: float = (kid_count / total_tickets) * 100

    print(f'Total tickets: {total_tickets}')
    print(f'{student_percent:.2f}% student tickets.')
    print(f'{standard_percent:.2f}% standard tickets.')
    print(f'{kid_percent:.2f}% kids tickets.')


if __name__ == '__main__':
    process_movie_tickets()
