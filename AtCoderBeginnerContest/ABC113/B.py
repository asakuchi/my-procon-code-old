N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

min_i = 0
min_temp = 100000000000000

for i, h in enumerate(H):

    temp = T - h * 0.006

    if abs(A - temp) < min_temp:
        min_i = i
        min_temp = abs(A - temp)

print(min_i + 1)
