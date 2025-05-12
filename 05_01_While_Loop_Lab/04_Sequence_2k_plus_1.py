# limit = int(input())
# value = 1
#
# while value <= limit:
#     print(value)
#     value = value * 2 + 1

limit = int(input())
value = 1

while True:
    if value > limit:
        break
    print(value)
    value = value * 2 + 1
