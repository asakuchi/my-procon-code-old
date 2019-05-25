import sys
def input():
    return sys.stdin.readline()[:-1]


N, M = map(int, input().split())
A = list(map(int, input().split()))

BC_list = []

for i in range(M):
    B, C = map(int, input().split())

    BC_list.append({
        'B': B,
        'C': C
    })

BC_list.sort(reverse=True, key=lambda x: x['C'])

A_last = min(A)

limit_count = 0

for pair in BC_list:

    if pair['C'] < A_last:
        break

    for _ in range(pair['B']):
        A.append(pair['C'])

    limit_count += pair['B']
    if limit_count > N:
        break

A.sort(reverse=True)

print(sum(A[0:N]))
