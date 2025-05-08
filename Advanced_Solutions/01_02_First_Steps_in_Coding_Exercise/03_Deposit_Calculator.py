def calculate_deposit_total(initial_amount: float, deposit_months: int, annual_interest: float) -> float:
    """
    Calculates the total amount after the deposit period with interest.

    Args:
        initial_amount: the amount of money deposited
        deposit_months: the duration of the deposit in months
        annual_interest: the annual interest rate (as percent)

    Returns:
        The total amount at the end of the deposit period
    """

    interest_per_month = (initial_amount * annual_interest / 100) / 12
    return initial_amount + deposit_months * interest_per_month


if __name__ == '__main__':
    deposit_input: float = float(input())
    months_input: int = int(input())
    interest_input: float = float(input())

    final_sum: float = calculate_deposit_total(
        initial_amount=deposit_input,
        deposit_months=months_input,
        annual_interest=interest_input
    )
    print(final_sum)
