import sys
def input():
    return sys.stdin.readline()[:-1]


N = int(input())

restaurants = []

for i in range(N):
    S, P = input().split()

    restaurants.append(
        {
            'S': S,
            'P': P,
            'number': i + 1
        }
    )

restaurants.sort(key=lambda x: (x['S'], -int(x['P'])))

for res in restaurants:
    print(res['number'])
