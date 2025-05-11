def calculate_histogram(count: int, values: list[int]) -> None:
    """
    Calculates and prints the percentage of numbers in five ranges.

    Args:
        count: Number of values.
        values: List of integers to analyze.

    Returns:
        Nothing. Prints the histogram.
    """
    if count == 0 or not values:
        for _ in range(5):
            print('0.00%')
        return

    below_200: int = 0
    from_200_to_399: int = 0
    from_400_to_599: int = 0
    from_600_to_799: int = 0
    from_800_and_up: int = 0

    for number in values:
        if number < 200:
            below_200 += 1
        elif number < 400:
            from_200_to_399 += 1
        elif number < 600:
            from_400_to_599 += 1
        elif number < 800:
            from_600_to_799 += 1
        else:
            from_800_and_up += 1

    percent_below_200: float = below_200 / count
    percent_200_to_399: float = from_200_to_399 / count
    percent_400_to_599: float = from_400_to_599 / count
    percent_600_to_799: float = from_600_to_799 / count
    percent_800_and_up: float = from_800_and_up / count

    print(f'{percent_below_200:.2%}')
    print(f'{percent_200_to_399:.2%}')
    print(f'{percent_400_to_599:.2%}')
    print(f'{percent_600_to_799:.2%}')
    print(f'{percent_800_and_up:.2%}')


if __name__ == '__main__':
    number_count: int = int(input())
    input_values: list[int] = [int(input()) for _ in range(number_count)]
    calculate_histogram(count=number_count, values=input_values)

#
#
# #############################################################################
#
# def calculate_histogram(count: int, values: list[int]) -> None:
#     """
#     Calculates and prints the percentage of numbers in five ranges.
#
#     Args:
#         count: Number of values.
#         values: List of integers to analyze.
#
#     Returns:
#         Nothing. Prints the histogram.
#     """
#     if count == 0 or not values:
#         for _ in range(5):
#             print('0.00%')
#         return
#
#     below_200: int = 0
#     from_200_to_399: int = 0
#     from_400_to_599: int = 0
#     from_600_to_799: int = 0
#     from_800_and_up: int = 0
#
#     for number in values:
#         if number < 200:
#             below_200 += 1
#         elif number < 400:
#             from_200_to_399 += 1
#         elif number < 600:
#             from_400_to_599 += 1
#         elif number < 800:
#             from_600_to_799 += 1
#         else:
#             from_800_and_up += 1
#
#     percent_below_200: float = (below_200 / count) * 100
#     percent_200_to_399: float = (from_200_to_399 / count) * 100
#     percent_400_to_599: float = (from_400_to_599 / count) * 100
#     percent_600_to_799: float = (from_600_to_799 / count) * 100
#     percent_800_and_up: float = (from_800_and_up / count) * 100
#
#     print(f'{percent_below_200:.2f}%')
#     print(f'{percent_200_to_399:.2f}%')
#     print(f'{percent_400_to_599:.2f}%')
#     print(f'{percent_600_to_799:.2f}%')
#     print(f'{percent_800_and_up:.2f}%')
#
#
# if __name__ == '__main__':
#     number_count: int = int(input())
#     input_values: list[int] = [int(input()) for _ in range(number_count)]
#     calculate_histogram(count=number_count, values=input_values)
