import sys

N = int(input())

x = []
y = []
h = []

for _ in range(N):
    t_x, t_y, t_h = map(int, input().split())
    x.append(t_x)
    y.append(t_y)
    h.append(t_h)

for i in range(101):
    for j in range(101):

        H = -1
        # 初期化
        for index, t_h in enumerate(h):
            if t_h != 0:
                H = abs(i - x[index]) + abs(j - y[index]) + t_h
                break

        for t_x, t_y, t_h in zip(x, y, h):
            if t_h == 0:
                if H > abs(i - t_x) + abs(j - t_y):
                    break
            elif H != abs(i - t_x) + abs(j - t_y) + t_h:
                break
        else:
            print(i, j, H)
            sys.exit()
