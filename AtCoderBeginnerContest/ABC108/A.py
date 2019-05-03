K = int(input())

if K % 2 == 0:
    print((K ** 2) // 4)
else:
    print((K // 2) * (K // 2 + 1))
