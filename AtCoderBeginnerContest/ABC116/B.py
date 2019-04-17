S = int(input())


def f(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1


memo = [0, S]
result = -1

for m in range(2, 1000000):

    a = f(memo[m - 1])
    memo.append(a)

    # print(memo)

    if a in memo[1:m - 1]:
        result = m
        break

print(result)
