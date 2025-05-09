def classify_speed(speed_value: float) -> None:
    """
    This tells how fast something is based on its speed.

    Args:
        speed_value: The speed to classify.

    Returns:
        None
    """
    if speed_value <= 10:
        result: str = 'slow'
    elif speed_value <= 50:
        result: str = 'average'
    elif speed_value <= 150:
        result: str = 'fast'
    elif speed_value <= 1000:
        result: str = 'ultra fast'
    else:
        result: str = 'extremely fast'

    print(result)


if __name__ == '__main__':
    input_speed: float = float(input())
    classify_speed(speed_value=input_speed)
