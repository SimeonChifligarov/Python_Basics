def convert_inches_to_cm(inches: float) -> float:
    """
    Converts inches to centimeters.
    If length_in_inches is less than 0, returns 0.
    Args:
        inches: length in inches

    Returns:
        The same length but in centimeters
    """
    if inches < 0:
        return 0.0
    return inches * 2.54


if __name__ == '__main__':
    input_inches: float = float(input())
    converted_length: float = convert_inches_to_cm(inches=input_inches)
    print(converted_length)
