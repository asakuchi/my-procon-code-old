#
# TLE
#

from functools import lru_cache

N = int(input())

a = []

for _ in range(N):
    a.append(int(input()))


@lru_cache(maxsize=None)
def rec(i, R, G, B):

    if i == N:
        if R < G + B and G < R + B and B < R + G:
            return 1
        else:
            return 0

    a_sum = rec(i + 1, R + a[i], G, B)
    b_sum = rec(i + 1, R, G + a[i], B)
    c_sum = rec(i + 1, R, G, B + a[i])

    return a_sum + b_sum + c_sum


print(rec(0, 0, 0, 0) % 998244353)
