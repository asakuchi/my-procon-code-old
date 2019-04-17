N, T = map(int, input().split())

answer = 'TLE'
INF = 100000000
min_cost = INF

for i in range(N):
    c, t = map(int, input().split())

    if t <= T and c < min_cost:
        min_cost = c

if min_cost == INF:
    print('TLE')
else:
    print(min_cost)
