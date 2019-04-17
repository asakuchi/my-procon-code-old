N, M = map(int, input().split())

like = {}

for i in range(N):
    foods = list(map(int, input().split()))

    K = foods.pop(0)

    for food in foods:
        if food in like:
            like[food] += 1
        else:
            like[food] = 1

count = 0;

for numOfLike in like.values():

    if numOfLike == N:
        count += 1

print(count)
