def convert_usd_to_bgn(amount_usd: float) -> float:
    """
    Converts USD to BGN using a fixed rate of 1.79549.

    Args:
        amount_usd: the amount in US dollars

    Returns:
        The equivalent amount in BGN
    """
    if amount_usd < 0:
        return 0.0

    exchange_rate = 1.79549
    return amount_usd * exchange_rate


if __name__ == '__main__':
    input_usd: float = float(input())
    result_bgn: float = convert_usd_to_bgn(amount_usd=input_usd)
    print(result_bgn)
