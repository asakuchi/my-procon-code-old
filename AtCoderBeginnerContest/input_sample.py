# inputを速く
import sys
def input():
    return sys.stdin.readline()[:-1]


# 複数
N, A, B, C = map(int, input().split())

# 一つ
N = int(input())

# 配列
N = list(map(int, input().split()))

# 整数 N 個 (改行区切り)
L = [int(input()) for i in range(N)]

# 整数 (縦 H 横 W の行列)
S = [list(map(int, input().split())) for i in range(H)]

########################

# 文字列
N, A, B, C = input().split()

# 文字列
N = input()

# 再起
import sys
sys.setrecursionlimit(10000000)

# メモ化
from functools import lru_cache
#@lru_cache(maxsize=None)
