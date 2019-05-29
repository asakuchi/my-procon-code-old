A, B, K = map(int, input().split())

result = set()

for n in range(A, A + K):
    result.add(n)

for n in range(B - K + 1, B + 1):
    result.add(n)

for n in sorted(list(result)):
    print(n)
