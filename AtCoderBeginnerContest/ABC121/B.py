N, M, C = map(int, input().split())

B = list(map(int, input().split()))

count = 0

for i in range(0, N):
    A = list(map(int, input().split()))

    sum_a = 0

    for j in range(0, M):

        sum_a += A[j] * B[j]

    sum_a += C

    if sum_a > 0:
        count += 1

print(count)
