import sys
def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())

l_max = 1
r_min = N

for i in range(M):
    L, R = map(int, input().split())

    l_max = max(l_max, L)
    r_min = min(r_min, R)

print(max(r_min - l_max + 1, 0))
