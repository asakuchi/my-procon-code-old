S = input()
T = input()

prev_T = T
result = 'No'

for i in range(len(T)):

    temp_T = prev_T[-1] + prev_T[0:-1]

    if temp_T == S:
        result = 'Yes'
        break

    prev_T = temp_T

print(result)
