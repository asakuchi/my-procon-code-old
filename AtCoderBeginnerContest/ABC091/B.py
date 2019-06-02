N = int(input())

words = {'na': 0}  # 選択しない

for i in range(N):

    s = input()

    if s in words:
        words[s] += 1
    else:
        words[s] = 1

M = int(input())

for i in range(M):

    t = input()

    if t in words:
        words[t] -= 1

print(max(words.values()))
