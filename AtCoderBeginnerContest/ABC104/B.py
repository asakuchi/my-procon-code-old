import re

S = input()

if S[0] == 'A' \
        and S[2:-1].count('C') == 1 \
        and re.match('^A[a-z]+C[a-z]+$', S):
    print('AC')
else:
    print('WA')
