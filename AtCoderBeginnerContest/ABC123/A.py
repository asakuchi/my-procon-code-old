a = [int(input()) for i in range(5)]
k = int(input())

exists = False

for i in a:
    for j in a:
        if abs(i - j) > k:
            exists = True

if exists:
    print(':(')
else:
    print('Yay!')
