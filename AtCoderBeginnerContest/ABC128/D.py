import copy

N, K = map(int, input().split())
V = list(map(int, input().split()))

INF = 10 ** 8


# mode 0: can pop left, pop right, drop
#      1: can pop right, drop
#      2: can drop
#      3: can not do anything
def rec(rest_ope, now_d, now_hand, mode):

    if rest_ope == 0:
        return sum(now_hand)

    max_price = -INF

    if len(now_d) > 0:
        if mode == 0:
            left_d = copy.copy(now_d)
            left_hand = copy.copy(now_hand)
            left_hand.append(left_d.pop(0))

            max_price = max(max_price, rec(rest_ope - 1, left_d, left_hand, 0))

        if mode <= 1:
            right_d = copy.copy(now_d)
            right_hand = copy.copy(now_hand)
            right_hand.append(right_d.pop(-1))

            max_price = max(max_price, rec(rest_ope - 1, right_d, right_hand, 1))

    if len(now_hand) > 0:
        if mode <= 2:
            drop_hand = copy.copy(now_hand)
            drop_hand.pop(drop_hand.index(min(drop_hand)))  # 最小値を削除

            max_price = max(max_price, rec(rest_ope - 1, now_d, drop_hand, 2))

    # do nothing
    max_price = max(max_price, rec(rest_ope - 1, now_d, now_hand, 3))

    return max_price


print(rec(K, V, [], 0))
