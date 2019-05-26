N, M = map(int, input().split())

s_list = []

for i in range(M):
    s = list(map(int, input().split()))
    s.pop(0)

    s_list.append(s)

p = list(map(int, input().split()))

on_off_list = [0] * N


def rec(index_on_off):

    if index_on_off == N:

        all_on = True

        for index_m in range(M):

            on_count = 0

            for s_value in s_list[index_m]:
                if on_off_list[s_value - 1] == 1:
                    on_count += 1

            if (on_count % 2) != p[index_m]:
                all_on = False

        if all_on:
            return 1
        else:
            return 0

    counter = 0

    on_off_list[index_on_off] = 0
    counter += rec(index_on_off + 1)

    on_off_list[index_on_off] = 1
    counter += rec(index_on_off + 1)

    return counter


print(rec(0))
