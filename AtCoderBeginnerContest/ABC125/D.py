N = int(input())
A = list(map(int, input().split()))

minus_count = 0

for a in A:
    if a < 0:
        minus_count += 1

total = 0
min_num = 10 ** 9

for a in A:
    total += abs(a)
    min_num = min(min_num, abs(a))

if minus_count % 2 == 1:
    total -= 2 * min_num

print(total)
