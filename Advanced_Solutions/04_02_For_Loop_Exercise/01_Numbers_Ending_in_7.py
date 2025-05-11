def print_numbers_ending_in_seven() -> None:
    """
    Prints numbers from 1 to 1000 that end with the digit 7.

    This function just goes through all numbers from 1 to 1000
    and prints the ones that end in 7.
    """
    # for number in range(1, 1001):
    #     if number % 10 == 7:
    #         print(number)

    # [print(number) for number in range(7, 1001, 10)]
    for number in range(7, 1001, 10):
        print(number)


if __name__ == '__main__':
    print_numbers_ending_in_seven()
