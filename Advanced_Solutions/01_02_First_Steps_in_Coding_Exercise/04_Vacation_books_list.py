def calculate_daily_reading_time(total_pages: int, pages_per_hour: int, days_to_finish: int) -> int:
    """
    Calculates how many hours per day someone needs to read to finish a book in time.

    Args:
        total_pages: total number of pages in the book
        pages_per_hour: how many pages can be read per hour
        days_to_finish: number of days to finish the book

    Returns:
        Required reading hours per day
    """
    total_hours = total_pages // pages_per_hour
    return total_hours // days_to_finish


if __name__ == '__main__':
    book_pages_input: int = int(input())
    reading_speed_input: int = int(input())
    deadline_days_input: int = int(input())

    hours_per_day: int = calculate_daily_reading_time(
        total_pages=book_pages_input,
        pages_per_hour=reading_speed_input,
        days_to_finish=deadline_days_input
    )
    print(hours_per_day)
