import fractions

N = int(input())
A = list(map(int, input().split()))

left = [0] * (N + 1)
right = [0] * (N + 1)

for i in range(N):
    left[i + 1] = fractions.gcd(A[i], left[i])

for i in reversed(range(N)):
    right[i] = fractions.gcd(A[i], right[i + 1])

max_gcd = 1

for i in range(N):

    l = left[i]
    r = right[i + 1]

    gcd_num = fractions.gcd(l, r)

    max_gcd = max(max_gcd, gcd_num)

print(max_gcd)
