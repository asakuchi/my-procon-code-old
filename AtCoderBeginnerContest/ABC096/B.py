ABC = list(map(int, input().split()))

K = int(input())

ABC.sort(reverse=True)

print(ABC[0] * (2 ** K) + ABC[1] + ABC[2])
