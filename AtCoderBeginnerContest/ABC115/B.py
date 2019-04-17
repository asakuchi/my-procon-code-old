N = int(input())
p = [int(input()) for i in range(N)]

p.sort(reverse=True)
total = 0

total += (p[0] // 2)

for i in range(1, N):
    total += p[i]

print(total)
