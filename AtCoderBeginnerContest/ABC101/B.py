N = int(input())

N_str = str(N)
Sn = 0

for c in N_str:

    Sn += int(c)

if N % Sn == 0:
    print('Yes')
else:
    print('No')
