def track_moving_boxes(width: int, length: int, height: int) -> None:
    """
    This function tracks how many boxes can be moved into an apartment
    based on the available cubic meters. Each box is 1 cubic meter.

    Args:
        width: the width of the space
        length: the length of the space
        height: the height of the space

    Returns:
        Nothing. Prints if space is enough or how much is missing.
    """
    total_volume: int = width * length * height
    used_volume: int = 0

    command: str = input()

    while command != 'Done':
        boxes: int = int(command)

        used_volume += boxes
        if used_volume > total_volume:
            shortage: int = used_volume - total_volume
            print(f'No more free space! You need {shortage} Cubic meters more.')
            return

        command = input()

    remaining: int = total_volume - used_volume
    print(f'{remaining} Cubic meters left.')


if __name__ == '__main__':
    width_input: int = int(input())
    length_input: int = int(input())
    height_input: int = int(input())
    track_moving_boxes(width=width_input, length=length_input, height=height_input)
