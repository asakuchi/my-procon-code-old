N, M = map(int, input().split())

path = {}

for i in range(1, N+1):
    path[i] = {}
    for j in range(1, N+1):
        if i != j:
            path[i][j] = False

print(path)

for i in range(M):
    A, B = map(int, input().split())

    path[A][B] = True
    path[B][A] = True

print(path)
