def calculate_remaining_salary(initial_salary: float, sites: list[str]) -> None:
    """
    Calculates the remaining salary after visiting distracting websites.

    Args:
        initial_salary: Starting salary before penalties.
        sites: List of website names visited.

    Returns:
        Nothing. Prints either remaining salary or a message if salary is lost.
    """
    salary_left: float = initial_salary
    penalties: dict[str, int] = {
        'Facebook': 150,
        'Instagram': 100,
        'Reddit': 50,
    }

    for site in sites:
        if site in penalties:
            salary_left -= penalties[site]

            if salary_left <= 0:
                print('You have lost your salary.')
                return

    print(int(salary_left))


if __name__ == '__main__':
    try:
        open_tabs: int = int(input())
        starting_salary: float = float(input())

        visited_sites: list[str] = []
        for _ in range(open_tabs):
            try:
                visited_sites.append(input())
            except EOFError:
                break  # Stop if fewer lines are provided

        calculate_remaining_salary(
            initial_salary=starting_salary,
            sites=visited_sites
        )

    except (ValueError, EOFError):
        print('Invalid or incomplete input.')
