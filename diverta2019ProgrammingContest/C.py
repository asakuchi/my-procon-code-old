import sys
def input():
    return sys.stdin.readline()[:-1]


N = int(input())

head_b_count = 0
tail_a_count = 0

head_b_tail_a_count = 0

total = 0

for _ in range(N):

    s = input()

    if s[0] == 'B':
        head_b_count += 1
    if s[-1] == 'A':
        tail_a_count += 1
    if s[0] == 'B' and s[-1] == 'A':
        head_b_tail_a_count += 1

    total += s.count('AB')

additional = min(head_b_count, tail_a_count)

if head_b_count == tail_a_count == head_b_tail_a_count != 0:
    additional -= 1

total += additional

print(total)
