def calculate_vowel_value_sum(input_text: str) -> int:
    """
    Calculates the sum of values of vowels in the input text based on predefined values.

    Args:
        input_text: the string to evaluate

    Returns:
        The total value of all vowels in the string
    """
    if not input_text:
        return 0

    vowel_values: dict[str, int] = {
        'a': 1,
        'e': 2,
        'i': 3,
        'o': 4,
        'u': 5,
    }

    total: int = sum([vowel_values[char] for char in input_text if char in vowel_values])
    return total


if __name__ == '__main__':
    user_string: str = input()
    result: int = calculate_vowel_value_sum(input_text=user_string)
    print(result)
