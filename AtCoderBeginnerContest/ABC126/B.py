S = input()

if S == '0000':
    print('NA')
else:
    if '01' <= S[0:2] <= '12' and (S[2:4] >= '13' or S[2:4] == '00'):
        print('MMYY')
    elif '01' <= S[2:4] <= '12' and S[0:2] >= '13' or S[0:2] == '00':
        print('YYMM')
    elif '01' <= S[0:2] <= '12' and '01' <= S[2:4] <= '12':
        print('AMBIGUOUS')
    else:
        print('NA')
