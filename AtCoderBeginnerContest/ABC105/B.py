N = int(input())

exists = False

for i in range(30):
    for j in range(20):
        if 4 * i + 7 * j == N:
            exists = True
            break

if exists:
    print('Yes')
else:
    print('No')
