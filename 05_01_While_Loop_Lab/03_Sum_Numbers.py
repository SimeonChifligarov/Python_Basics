# target_sum = int(input())
# current_sum = 0
#
# while current_sum < target_sum:
#     number = int(input())
#     current_sum += number
#
# print(current_sum)

target_sum = int(input())
current_sum = 0

while True:
    if current_sum >= target_sum:
        break

    number = int(input())
    current_sum += number

print(current_sum)
