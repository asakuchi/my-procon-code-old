N = int(input())
h = list(map(int, input().split()))


def rec(array):

    count = 0

    if sum(array) == 0:
        return count

    if 0 in array:
        none = array.index(0)

        count += rec(array[:none])
        count += rec(array[none + 1:])

    else:
        min_num = min(array)

        for i in range(len(array)):
            array[i] -= min_num
        count += min_num

        count += rec(array)

    return count


print(rec(h))
