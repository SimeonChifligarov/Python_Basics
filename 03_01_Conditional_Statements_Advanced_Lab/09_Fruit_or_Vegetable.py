product_input = input()

if product_input in ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']:
    category = 'fruit'
# if product_input == 'banana' or product_input == 'apple' or product_input == 'kiwi' or product_input == 'cherry' or product_input == 'lemon' or product_input == 'grapes':  # noqa E501
#     category = 'fruit'

elif product_input in ['tomato', 'cucumber', 'pepper', 'carrot']:
    category = 'vegetable'
# elif product_input == 'tomato' or product_input == 'cucumber' or product_input == 'pepper' or product_input == 'carrot':  # noqa E501
#     category = 'vegetable'

else:
    category = 'unknown'

print(category)
