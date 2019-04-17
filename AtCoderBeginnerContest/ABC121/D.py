def f(a, b):
    if a > 0:
        a -= 1

    return g(a) ^ g(b)


def g(num):

    others = 0

    if num % 2 == 0:
        if (num // 2) % 2 != 0:
            others = 1

        return num ^ others
    else:
        if ((num - 1) // 2) % 2 != 0:
            others = 1

        return num ^ others ^ num - 1


A, B = map(int, input().split())

result = f(A, B)

print(result)
