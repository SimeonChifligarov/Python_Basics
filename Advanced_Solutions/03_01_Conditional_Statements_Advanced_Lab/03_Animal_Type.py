def classify_animal(animal_name: str) -> str:
    """
    Returns the animal class based on the given name.

    Args:
        animal_name: A string representing the animal name.

    Returns:
        A string - 'mammal', 'reptile', or 'unknown'.
    """
    mammals: set[str] = {'dog', }
    reptiles: set[str] = {'crocodile', 'tortoise', 'snake', }

    if animal_name in mammals:
        return 'mammal'

    if animal_name in reptiles:
        return 'reptile'

    return 'unknown'


if __name__ == '__main__':
    input_animal: str = input()
    result: str = classify_animal(animal_name=input_animal)
    print(result)
