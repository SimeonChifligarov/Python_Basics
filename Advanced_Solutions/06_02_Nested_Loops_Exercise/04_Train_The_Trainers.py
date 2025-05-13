def train_the_trainers(jury_count: int) -> None:
    """
    Reads presentation names and jury scores. Prints average for each presentation
    and final average from all presentations.

    Args:
        jury_count: Number of jury members scoring each presentation.
    """
    if jury_count < 1:
        return

    total_score: float = 0.0
    total_grades: int = 0

    while True:
        presentation_name: str = input()
        if presentation_name == 'Finish':
            break

        scores: list[float] = [float(input()) for _ in range(jury_count)]
        average: float = sum(scores) / jury_count

        print(f'{presentation_name} - {average:.2f}.')
        total_score += sum(scores)
        total_grades += jury_count

    if total_grades > 0:
        final_average: float = total_score / total_grades
        print(f"Student's final assessment is {final_average:.2f}.")


if __name__ == '__main__':
    jury_size: int = int(input())
    train_the_trainers(jury_count=jury_size)
