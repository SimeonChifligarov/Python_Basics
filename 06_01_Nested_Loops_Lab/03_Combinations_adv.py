n = int(input())
count = 0

for x in range(n + 1):
    for y in range(n + 1):
        z = n - x - y
        if 0 <= z <= n:
            count += 1

print(count)
