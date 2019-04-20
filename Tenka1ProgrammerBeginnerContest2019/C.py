#
# WA
#

N = int(input())
S = input()

W = '.'
B = '#'

first_B = S.find(B)

print(min(S[first_B:].count(W), S[first_B:].count(B)))
