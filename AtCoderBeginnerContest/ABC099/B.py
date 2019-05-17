a, b = map(int, input().split())

num = 0

for i in range(1, b - a + 1):
    num += i

print(num - b)
