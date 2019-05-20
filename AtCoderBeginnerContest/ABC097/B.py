import sys

X = int(input())

for i in reversed(range(1, X + 1)):
    for j in range(1, i + 1):
        for k in range(2, i + 10):

            num = j ** k

            if num == i:
                print(num)
                sys.exit()

            if num > i:
                break
