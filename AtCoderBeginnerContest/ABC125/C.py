#TLE

import fractions

N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

max_gcd = 1

for i in range(N):
    gcd_num = -1

    for j, a in enumerate(A):
        if i == j:
            continue

        if gcd_num == -1:
            gcd_num = a
            continue

        gcd_num = fractions.gcd(gcd_num, a)

    max_gcd = max(max_gcd, gcd_num)

print(max_gcd)
