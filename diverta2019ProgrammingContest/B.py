R, G, B, N = map(int, input().split())

total = 0

for r in range(N // R + 1):
    for g in range((N - r * R) // G + 1):
        if (N - r * R - g * G) >= 0 and (N - r * R - g * G) % B == 0:
            total += 1

print(total)
