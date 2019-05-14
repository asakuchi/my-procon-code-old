N, K = map(int, input().split())
A = list(map(int, input().split()))

one_index = A.index(1)

total = 0

if one_index != 0:
    total += (len(A[0:one_index]) // (K - 1))

if one_index != len(A):
    total += max(0, len(A[one_index:]) // (K - 1))

print(max(0, len(A[0:one_index]) // (K - 1)) + max(0, len(A[one_index:]) // (K - 1)))

