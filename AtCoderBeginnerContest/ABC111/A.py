N = input()

N = N.replace('1', 'x')
N = N.replace('9', '1')
N = N.replace('x', '9')

print(int(N))
