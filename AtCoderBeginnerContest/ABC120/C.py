S = input()

count_0 = S.count('0')
count_1 = S.count('1')

print(min(count_0, count_1) * 2)
