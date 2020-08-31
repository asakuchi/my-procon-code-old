S = input()
T = input()

answer = len(T)

for i in range(0, len(S) - len(T) + 1):

    diff = 0

    for j in range(0, len(T)):
        if T[j] != S[i + j]:
            diff += 1

    answer = min(answer, diff)

print(answer)
