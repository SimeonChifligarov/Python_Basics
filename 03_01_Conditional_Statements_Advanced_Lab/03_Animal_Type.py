animal_input = input()

if animal_input in ['dog', ]:
    result = 'mammal'
# if animal_input == 'dog':
#     result = 'mammal'

elif animal_input in ['crocodile', 'tortoise', 'snake', ]:
    result = 'reptile'
# elif animal_input == 'crocodile' or animal_input == 'tortoise' or animal_input == 'snake':
#     result = 'reptile'

else:
    result = 'unknown'

print(result)
