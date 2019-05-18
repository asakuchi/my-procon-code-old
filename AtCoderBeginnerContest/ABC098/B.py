N = int(input())
S = input()

max_number = 0

for i in range(1, N):

    pre = S[0:i]
    post = S[i:]

    pre_dic = {}
    post_dic = {}

    for c in pre:
        pre_dic[c] = True

    for c in post:
        post_dic[c] = True

    number = 0

    for c in post_dic:
        if c in pre_dic:
            number += 1

    max_number = max(max_number, number)

print(max_number)
