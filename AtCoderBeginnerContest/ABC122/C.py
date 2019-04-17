import sys


def input():
    return sys.stdin.readline()[:-1]


N, Q = map(int, input().split())
S = input()

hit = [0] * N

for i in range(0, N - 1):
    hit[i + 1] = hit[i]

    if S[i:i+2] == 'AC':
        hit[i + 1] += 1

for _ in range(0, Q):
    l, r = map(int, input().split())
    result = hit[r - 1] - hit[l - 1]
    print(result)

