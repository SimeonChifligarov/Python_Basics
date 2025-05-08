def calculate_aquarium_volume(length_cm: int, width_cm: int, height_cm: int, percent_filled: float) -> float:
    """
    Calculates how many liters of water are needed to fill the aquarium,
    considering that some percent of the volume is occupied.

    Args:
        length_cm: the length of the aquarium in cm
        width_cm: the width of the aquarium in cm
        height_cm: the height of the aquarium in cm
        percent_filled: the percentage of the volume occupied by other items

    Returns:
        The usable volume of water in liters
    """
    total_volume_cm3: float = length_cm * width_cm * height_cm
    total_volume_liters: float = total_volume_cm3 / 1000
    usable_volume: float = total_volume_liters * (1 - percent_filled / 100)

    return usable_volume


if __name__ == '__main__':
    input_length: int = int(input())
    input_width: int = int(input())
    input_height: int = int(input())
    input_percent: float = float(input())

    water_needed: float = calculate_aquarium_volume(
        length_cm=input_length,
        width_cm=input_width,
        height_cm=input_height,
        percent_filled=input_percent
    )
    print(water_needed)
