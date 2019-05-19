import sys
def input():
    return sys.stdin.readline()[:-1]


N = int(input())

vertex = {}

colors = [-1] * (N + 1)

for i in range(N - 1):
    u, v, w = map(int, input().split())

    if u in vertex:
        vertex[u][v] = w
    else:
        vertex[u] = {v: w}

for i in range(1, N):
    ver = vertex[i]

    if colors[i] != -1:
        for key in ver:
            if ver[key] % 2 == 0:
                colors[key] = colors[i]
            else:
                if colors[i] == 1:
                    colors[key] = 0
                else:
                    colors[key] = 1
    else:

for i in range(1, N):
    print(colors[i])
