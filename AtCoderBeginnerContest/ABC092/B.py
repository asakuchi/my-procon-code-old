N = int(input())
D, X = map(int, input().split())

A = [int(input()) for i in range(N)]

total = X

for ai in A:
    for d in range(1, D + 1):
        if (d - 1) % ai == 0:
            total += 1

print(total)
