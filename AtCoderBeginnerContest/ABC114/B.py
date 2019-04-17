S = input()

min_val = 9999999999

for i in range(0, len(S) - 2):
    sub = int(S[i:i+3])

    min_val = min(min_val,abs(753 - sub))

print(min_val)
