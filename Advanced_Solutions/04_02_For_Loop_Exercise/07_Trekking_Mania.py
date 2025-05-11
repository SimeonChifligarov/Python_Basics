def calculate_climbers_distribution(group_sizes: list[int]) -> None:
    """
    Calculates and prints percentage of climbers for each mountain peak.

    Args:
        group_sizes: List with the size of each group.

    Returns:
        Nothing. Prints the percentage for each peak.
    """
    musala: int = 0
    montblanc: int = 0
    kilimanjaro: int = 0
    k2: int = 0
    everest: int = 0
    total_climbers: int = sum(group_sizes)

    for size in group_sizes:
        if size <= 5:
            musala += size
        elif size <= 12:
            montblanc += size
        elif size <= 25:
            kilimanjaro += size
        elif size <= 40:
            k2 += size
        else:
            everest += size

    musala_percent: float = musala / total_climbers
    montblanc_percent: float = montblanc / total_climbers
    kilimanjaro_percent: float = kilimanjaro / total_climbers
    k2_percent: float = k2 / total_climbers
    everest_percent: float = everest / total_climbers

    print(f'{musala_percent:.2%}')
    print(f'{montblanc_percent:.2%}')
    print(f'{kilimanjaro_percent:.2%}')
    print(f'{k2_percent:.2%}')
    print(f'{everest_percent:.2%}')


if __name__ == '__main__':
    total_groups: int = int(input())
    all_group_sizes: list[int] = [int(input()) for _ in range(total_groups)]

    calculate_climbers_distribution(group_sizes=all_group_sizes)
