needs = {
    1: 2,
    2: 5,
    3: 5,
    4: 4,
    5: 5,
    6: 6,
    7: 3,
    8: 7,
    9: 6,
}

N, M = map(int, input().split())
A = list(map(int, input().split()))

most_low_cost = 100

map_need = {}

for num in A:
    map_need[num] = needs[num]

max_num = max(map_need)
min_num = min(map_need)

cost_performance_list = []

for num in map_need:
    cost_performance_list.append([num, map_need[num]])

cost_performance_list = sorted(cost_performance_list, key=lambda x: x[0] // x[1], reverse=True)

print(cost_performance_list)

print("N" + str(N))

# 一番上の桁
if N > map_need[max_num]:
    print(max_num, end="")
    N -= map_need[max_num]

print("N" + str(N))

# コスパが良い
for cp in cost_performance_list:
    number = cp[0]
    cost = cp[1]

    while N > cost:
        print(number, end="")
        N -= cost

        print("N" + str(N))




