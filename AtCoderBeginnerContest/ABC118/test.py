my_dic = [
    [1, 10],
    [2, 2],
    [3, 3],
    [4, 400],
    [5, 3],
]

sorted_dic = sorted(my_dic, key=lambda x: x[1] * x[0], reverse=True)

print(sorted_dic)
