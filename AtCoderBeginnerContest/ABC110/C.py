S = input()
T = input()

char_map = {}
char_map_t = {}

result = 'Yes'

for s, t in zip(S, T):
    if s in char_map:
        if t == char_map[s]:
            continue
        else:
            result = 'No'
            break
    else:
        char_map[s] = t

    if t in char_map_t:
        if s == char_map_t[t]:
            continue
        else:
            result = 'No'
            break
    else:
        char_map_t[t] = s

print(result)
