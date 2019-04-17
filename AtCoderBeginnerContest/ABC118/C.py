def gcd(m: int, n: int):

    if n == 0:
        return m

    return gcd(n, m % n)


N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

num = A[0]

for i in range(1, N):

    if A[i] > num:
        big = A[i]
        small = num
    else:
        big = num
        small = A[i]

    num = gcd(big, small)

print(num)
