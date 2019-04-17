N = int(input())

candidate = [111,222,333,444,555,666,777,888,999]

for c in candidate:
    if N <= c:
        print(c)
        break
