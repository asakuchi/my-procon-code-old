import sys
def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())

P = []
Y = []
for _ in range(M):
    p, y = map(int, input().split())
    P.append(p)
    Y.append(y)

pref = {}

for i in range(M):

    if P[i] not in pref:
        pref[P[i]] = []

    pref[P[i]].append({
        'city': i,
        'year': Y[i],
    })

for key in pref:
    pref[key].sort(key=lambda x: x['year'])

# print(pref)

city = {}

for key in pref:
    for i in range(len(pref[key])):
        city[pref[key][i]['city']] = {'order': i + 1}

# print(pref)

# output
for i in range(M):
    print(format(P[i], '06d') + format(city[i]['order'], '06d'))
