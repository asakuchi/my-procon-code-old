S = input()

y, m, d = map(int, S.split('/'))

if y == 2019 and m <= 4:
    print('Heisei')
else:
    print('TBD')
