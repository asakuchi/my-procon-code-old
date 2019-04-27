A, B, T = map(int, input().split())

total = 0

for i in range(1, 1000):

    if A * i < T + 1:
        total += B

print(total)
