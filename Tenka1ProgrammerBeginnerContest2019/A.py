A, B, C = map(int, input().split())

if A == C or B == C:
    print('Yes')
elif A < B:
    if A <= C and C <= B:
        print('Yes')
    else:
        print('No')
else:
    if B <= C and C <= A:
        print('Yes')
    else:
        print('No')
