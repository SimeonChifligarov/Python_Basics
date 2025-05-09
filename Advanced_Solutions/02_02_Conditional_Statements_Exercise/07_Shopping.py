def can_afford_computer_parts(
        budget: float,
        video_cards_count: int,
        processor_count: int,
        ram_count: int
) -> str:
    """
    This checks if the budget is enough to buy specified quantities of video cards, processors, and RAM.

    Args:
        budget: The total amount of money available.
        video_cards_count: The number of video cards.
        processor_count: The number of processors.
        ram_count: The number of RAM units.

    Returns:
        A message indicating whether the budget is enough and how much is left or missing.
    """
    video_card_price: float = 250
    total_video_card_price: float = video_cards_count * video_card_price
    processor_price: float = total_video_card_price * 0.35
    ram_price: float = total_video_card_price * 0.1

    total_cost: float = (
            total_video_card_price +
            processor_count * processor_price +
            ram_count * ram_price
    )

    if video_cards_count > processor_count:
        total_cost *= 0.85

    remaining_money: float = budget - total_cost

    if remaining_money >= 0:
        return f'You have {remaining_money:.2f} leva left!'
    return f'Not enough money! You need {abs(remaining_money):.2f} leva more!'


if __name__ == '__main__':
    total_budget: float = float(input())
    cards: int = int(input())
    processors: int = int(input())
    ram_modules: int = int(input())

    result: str = can_afford_computer_parts(
        budget=total_budget,
        video_cards_count=cards,
        processor_count=processors,
        ram_count=ram_modules
    )
    print(result)
