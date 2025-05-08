def calculate_rectangle_area(side_1: int, side_2: int) -> int:
    """
    Calculates the area of a rectangle using two side lengths.
    If some of the sides is less or equal to 0, returns 0
    Args:
        side_1: one side of the rectangle
        side_2: the other side of the rectangle

    Returns:
        The area of the rectangle
    """
    if side_1 <= 0 or side_2 <= 0:
        return 0
    return side_1 * side_2


if __name__ == '__main__':
    value_a: int = int(input())
    value_b: int = int(input())
    result_area: int = calculate_rectangle_area(side_1=value_a, side_2=value_b)
    print(result_area)
