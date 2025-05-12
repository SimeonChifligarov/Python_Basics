# user = input()
# password = input()
# attempt = input()
#
# while attempt != password:
#     attempt = input()
#
# print(f'Welcome {user}!')

user = input()
password = input()

while True:
    attempt = input()
    if attempt == password:
        break

print(f'Welcome {user}!')
