import math


def convert_radians_to_degrees(angle_radians: float) -> float:
    """
    Converts radians to degrees.

    Args:
        angle_radians: an angle given in radians

    Returns:
        The angle converted to degrees
    """
    return angle_radians * 180 / math.pi


if __name__ == '__main__':
    input_radians: float = float(input())
    result_degrees: float = convert_radians_to_degrees(angle_radians=input_radians)
    print(result_degrees)
