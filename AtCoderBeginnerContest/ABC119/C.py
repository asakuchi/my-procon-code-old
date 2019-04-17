N, A, B, C = map(int, input().split())

L = [int(input()) for i in range(N)]

INF = 10 ** 9


# 最小MPを返す
def rec(index, a, b, c):

    # 終了条件
    if index >= N:
        if a != 0 and b != 0 and c != 0:
            # 不足分は延長魔法、短縮魔法を使う
            return abs(A - a) + abs(B - b) + abs(C - c)
        else:
            return INF

    # L[index] をAの材料に使う
    cost_mp_a = 10 if a != 0 else 0
    result_a = rec(index + 1, a + L[index], b, c) + cost_mp_a

    # L[index] をBの材料に使う
    cost_mp_b = 10 if b != 0 else 0
    result_b = rec(index + 1, a, b + L[index], c) + cost_mp_b

    # L[index] をCの材料に使う
    cost_mp_c = 10 if c != 0 else 0
    result_c = rec(index + 1, a, b, c + L[index]) + cost_mp_c

    # L[index] を使わない
    result_none = rec(index + 1, a, b, c)

    return min(result_a, result_b, result_c, result_none)


print(rec(0, 0, 0, 0))
