A, B = map(int, input().split())

exists = 'No'

for c in range(1, 4):
    if (A * B * c) % 2 == 1:
        exists = 'Yes'
        break

print(exists)
