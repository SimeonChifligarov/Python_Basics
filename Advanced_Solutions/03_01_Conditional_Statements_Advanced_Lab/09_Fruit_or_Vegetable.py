def classify_product(product_name: str) -> str:
    """
    Classifies the given product as fruit, vegetable, or unknown.

    Args:
        product_name: The name of the product.

    Returns:
        A string - 'fruit', 'vegetable', or 'unknown'.
    """
    fruits: set[str] = {'banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes', }
    vegetables: set[str] = {'tomato', 'cucumber', 'pepper', 'carrot', }

    if product_name in fruits:
        return 'fruit'

    if product_name in vegetables:
        return 'vegetable'

    return 'unknown'


if __name__ == '__main__':
    input_product: str = input()
    result: str = classify_product(product_name=input_product)
    print(result)
