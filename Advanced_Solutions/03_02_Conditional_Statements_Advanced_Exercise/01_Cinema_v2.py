def calculate_total_income(session_type: str, row_count: int, column_count: int) -> float:
    """
    Calculates the total ticket income based on session type and seat layout.

    Args:
        session_type: The type of the movie session.
        row_count: Number of rows in the cinema hall.
        column_count: Number of seats per row.

    Returns:
        Total ticket income for a full cinema hall.
    """
    if session_type not in {'Premiere', 'Normal', 'Discount'}:
        return 0.0

    price_map: dict[str, float] = {
        'Premiere': 12.0,
        'Normal': 7.5,
        'Discount': 5.0
    }

    total_seats: int = row_count * column_count
    return total_seats * price_map[session_type]


if __name__ == '__main__':
    projection_type_input: str = input()
    rows_input: int = int(input())
    columns_input: int = int(input())

    revenue: float = calculate_total_income(
        session_type=projection_type_input,
        row_count=rows_input,
        column_count=columns_input
    )
    print(f'{revenue:.2f} leva')
