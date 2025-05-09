def classify_number(number_input: int) -> None:
    """
    This checks if the number is less than 100, between 100 and 200, or greater than 200.

    Args:
        number_input: The number to classify.

    Returns:
        None
    """
    if number_input < 100:
        result = 'Less than 100'
    elif number_input > 200:
        result = 'Greater than 200'
    else:
        result = 'Between 100 and 200'

    print(result)


if __name__ == '__main__':
    user_number: int = int(input())
    classify_number(number_input=user_number)
