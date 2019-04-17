S = input()

odd = S[0::2]
even = S[1::2]

odd_0_count = odd.count('0')
odd_1_count = odd.count('1')

even_0_count = even.count('0')
even_1_count = even.count('1')

# 奇数を0に、偶数を1にする
pattern1 = odd_1_count + even_0_count
# 奇数を1に、偶数を0にする
pattern2 = odd_0_count + even_1_count

print(min(pattern1,pattern2))
