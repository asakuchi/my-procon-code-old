import math
a = [int(input()) for i in range(5)]

sum_num = 0

delta = 10

for num in a:
    if num % 10 != 0 and num % 10 < delta:
        delta = num % 10
    sum_num += math.ceil(num / 10) * 10

print(sum_num - 10 + delta)
