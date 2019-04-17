N, K = map(int, input().split())
h = [int(input()) for i in range(N)]

h.sort()

min_h = 1000000000

for i in range(K - 1, N):
    min_h = min(min_h, h[i] - h[i - K + 1])

print(min_h)
