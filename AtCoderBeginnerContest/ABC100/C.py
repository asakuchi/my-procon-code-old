N = int(input())
a = list(map(int, input().split()))

total = 0

for ai in a:
    while ai % 2 == 0:
        ai /= 2
        total += 1

print(total)
