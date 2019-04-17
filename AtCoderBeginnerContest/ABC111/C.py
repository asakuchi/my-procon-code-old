from collections import Counter

N = int(input())
v = list(map(int, input().split()))

print(v[0::2])

even = Counter(v[0::2])
odd = Counter(v[1::2])

most_even = even.most_common()
most_odd = odd.most_common()

print(most_even)
print(most_odd)

different = False

for e in most_even:
    for o in most_odd:
        if e[0] != o[0]:
            different = True

print(different)

if most_odd != most_even:
    pass

