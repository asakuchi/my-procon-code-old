H, W = map(int, input().split())
h1, w1 = map(int, input().split())

print(H * W - h1 * W - w1 * H + h1 * w1)
