from math import pi


def calculate_area(shape_type: str) -> str:
    """
    This calculates the area of a geometric figure and returns it as a formatted string.

    Args:
        shape_type: The type of the shape ('square', 'rectangle', 'circle', 'triangle')

    Returns:
        A string with the area rounded to 3 digits.

    Raises:
        ValueError: If the shape type is not supported.
    """
    if shape_type == 'square':
        side_length: float = float(input())
        area: float = side_length * side_length
    elif shape_type == 'rectangle':
        length: float = float(input())
        width: float = float(input())
        area = length * width
    elif shape_type == 'circle':
        radius: float = float(input())
        area = pi * radius * radius
    elif shape_type == 'triangle':
        base: float = float(input())
        height: float = float(input())
        area = (base * height) / 2
    else:
        raise ValueError('Unsupported shape type')

    return f'{area:.3f}'


if __name__ == '__main__':
    figure_type: str = input()
    result: str = calculate_area(shape_type=figure_type)
    print(result)
