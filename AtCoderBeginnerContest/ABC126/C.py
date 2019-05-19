N, K = map(int, input().split())

sigma = 0

for i in range(1, N + 1):
    coin = 0

    while i * (2 ** coin) < K:
        coin += 1

    sigma += ((1 / N) * (0.5 ** coin))

print(sigma)
