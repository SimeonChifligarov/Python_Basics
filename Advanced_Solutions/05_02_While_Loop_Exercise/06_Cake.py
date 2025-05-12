def track_cake_distribution(width: int, length: int) -> None:
    """
    This function calculates if the birthday cake is enough
    for all guests based on the number of pieces they take.

    Args:
        width: width of the cake in cm
        length: length of the cake in cm

    Returns:
        Nothing. Prints result messages about remaining or missing cake.
    """
    total_pieces: int = width * length
    taken_pieces: int = 0

    command: str = input()

    while command != 'STOP':
        current_pieces: int = int(command)
        taken_pieces += current_pieces
        if taken_pieces > total_pieces:
            shortage: int = taken_pieces - total_pieces
            print(f'No more cake left! You need {shortage} pieces more.')
            return

        command = input()

    remaining: int = total_pieces - taken_pieces
    print(f'{remaining} pieces are left.')


if __name__ == '__main__':
    cake_width_input: int = int(input())
    cake_length_input: int = int(input())
    track_cake_distribution(width=cake_width_input, length=cake_length_input)
