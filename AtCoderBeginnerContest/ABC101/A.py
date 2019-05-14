S = input()

number = 0

for c in S:
    if c == '+':
        number += 1
    else:
        number -= 1

print(number)
