N = int(input())


def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    divisors.sort()
    return divisors


div = make_divisors(N)
total = 0

for num in div:
    if num == 1:
        continue

    if N // (num - 1) == N % (num - 1):
        total += (num - 1)

print(total)
