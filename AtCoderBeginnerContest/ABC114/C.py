N = int(input())


def count753(number):

    if int(number) > N:
        return 0

    if number == '0':
        number = ''

    if '7' not in number or '5' not in number or '3' not in number:
        result = 0
    else:
        result = 1

    result += count753('7' + number)
    result += count753('5' + number)
    result += count753('3' + number)

    return result


print(count753('0'))
