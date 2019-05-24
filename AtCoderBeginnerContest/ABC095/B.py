N, X = map(int, input().split())

min_m = 1000

for i in range(N):
    mi = int(input())

    min_m = min(min_m, mi)

    X -= mi

print(N + X // min_m)
