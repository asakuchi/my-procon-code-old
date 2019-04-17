# greatest common divisor


def gcd(m: int, n: int):

    if n == 0:
        return m

    return gcd(n, m % n)


num = gcd(12, 4)

print(num)
