S = input()

max_length = 0

for i in range(0, len(S)):
    for j in range(i + 1, len(S) + 1):
        sub = S[i:j]
        #print(sub.replace('ACGT', ''))
        if len(sub.translate(str.maketrans({'A':'','C':'','G':'','T':''}))) == 0:
            max_length = max(len(sub), max_length)


print(max_length)

