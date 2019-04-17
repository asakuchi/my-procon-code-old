N, K = map(int, input().split())
S = input()

continuous_list = [0] * N

for i in range(N):
    tmp_K = K
    length = 0
    zero_mode = False  # 連続した0

    # print("i" + str(i))

    for j in range(i, N):
        # print("j" + str(j))

        if S[j] == '1':
            zero_mode = False
            length += 1
        else:
            if zero_mode:
                length += 1
            else:
                if tmp_K > 0:
                    tmp_K -= 1
                    length += 1
                    zero_mode = True
                else:
                    break

    # print("length:" + str(length))
    continuous_list[i] = length


# print(continuous_list)

print(max(continuous_list))
