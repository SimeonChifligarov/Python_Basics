def perform_operation(value_1: int, value_2: int, operator_symbol: str) -> str:
    """
    Performs an arithmetic operation between two integers and returns a formatted result.

    Args:
        value_1: First integer number.
        value_2: Second integer number.
        operator_symbol: One of '+', '-', '*', '/', '%'.

    Returns:
        A string describing the result of the operation or an error if dividing by zero.
    """
    if operator_symbol in {'/', '%'} and value_2 == 0:
        return f'Cannot divide {value_1} by zero'

    operations: dict[str, callable] = {
        '+': lambda a, b: f'{a} + {b} = {a + b} - {"even" if (a + b) % 2 == 0 else "odd"}',
        '-': lambda a, b: f'{a} - {b} = {a - b} - {"even" if (a - b) % 2 == 0 else "odd"}',
        '*': lambda a, b: f'{a} * {b} = {a * b} - {"even" if (a * b) % 2 == 0 else "odd"}',
        '/': lambda a, b: f'{a} / {b} = {a / b:.2f}',
        '%': lambda a, b: f'{a} % {b} = {a % b}',
    }

    operation = operations.get(operator_symbol)

    if operation is None:
        return 'Invalid operator'

    return operation(value_1, value_2)


if __name__ == '__main__':
    number_1_input: int = int(input())
    number_2_input: int = int(input())
    operation_input: str = input()

    output: str = perform_operation(
        value_1=number_1_input,
        value_2=number_2_input,
        operator_symbol=operation_input
    )
    print(output)
