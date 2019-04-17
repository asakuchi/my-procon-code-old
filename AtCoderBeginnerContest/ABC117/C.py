N, M = map(int, input().split())

X = list(map(int, input().split()))

X.sort()

# print(X)

L = [0] * (M - 1)

for i in range(0, M - 1):
    L[i] = X[i + 1] - X[i]

# print(L)

L.sort(reverse=True)

result = X[-1] - X[0] - sum(L[:N - 1])

print(result)
