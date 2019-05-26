import sys
def input():
    return sys.stdin.readline()[:-1]


N, Q = map(int, input().split())

constructions = []

for _ in range(N):
    S, T, X = map(int, input().split())

    constructions.append(
        {
            'S': S,
            'T': T,
            'X': X
        }
    )

D = []

for _ in range(Q):
    D.append(int(input()))

print(constructions)
print(D)
