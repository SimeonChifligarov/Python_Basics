def print_multiplication_table() -> None:
    """
    Prints the multiplication table from 1 to 10.

    Returns:
        None
    """
    for multiplicand in range(1, 11):
        for multiplier in range(1, 11):
            result = multiplicand * multiplier
            print(f'{multiplicand} * {multiplier} = {result}')


if __name__ == '__main__':
    print_multiplication_table()
