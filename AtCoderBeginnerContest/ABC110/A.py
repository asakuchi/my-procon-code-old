N = list(map(int, input().split()))

N.sort(reverse=True)

print(int(str(N[0]) + str(N[1])) + N[2])

