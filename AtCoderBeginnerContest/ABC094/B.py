N, M, X = map(int, input().split())
A = list(map(int, input().split()))

costs = [0] * (N + 1)

for val in A:
    costs[val] = 1

print(min(sum(costs[0:X]), sum(costs[X:-1])))
