N = int(input())

W = input()

last = W[-1]
word_list = {W}
result = 'Yes'

for i in range(1, N):
    W = input()

    if W[0] == last:
        last = W[-1]
    else:
        result = 'No'

    if W in word_list:
        result = 'No'
    else:
        word_list.add(W)

print(result)
