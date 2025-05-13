def print_building_layout(total_floors: int, rooms_per_floor: int) -> None:
    """
    Prints the room numbers of a building based on floor and room rules.

    Args:
        total_floors: total number of floors in the building
        rooms_per_floor: number of rooms per floor

    Returns:
        None
    """
    if total_floors <= 0 or rooms_per_floor <= 0:
        return

    for current_floor in range(total_floors, 0, -1):
        if current_floor == total_floors:
            room_prefix = 'L'
        elif current_floor % 2 == 0:
            room_prefix = 'O'
        else:
            room_prefix = 'A'

        floor_layout = [
            f'{room_prefix}{current_floor}{room_number}'
            for room_number in range(rooms_per_floor)
        ]

        print(' '.join(floor_layout))


if __name__ == '__main__':
    floors_input: int = int(input())
    rooms_input: int = int(input())
    print_building_layout(total_floors=floors_input, rooms_per_floor=rooms_input)
