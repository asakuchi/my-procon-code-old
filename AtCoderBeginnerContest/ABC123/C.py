import math

N = int(input())
a = [int(input()) for i in range(5)]

min_num = min(a)

print(math.ceil(N / min_num) + 4)
