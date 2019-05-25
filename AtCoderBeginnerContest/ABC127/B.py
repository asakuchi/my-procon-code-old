r, D, x2000 = map(int, input().split())

xi = x2000

for i in range(10):
    xi1 = r * xi - D
    print(xi1)
    xi = xi1

