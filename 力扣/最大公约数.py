def greatest_common_divisor(x, y):
    big = max(x, y)
    small = min(x, y)
    if big % small == 0:
        return small
    for i in range(small // 2, 0, -1):
        if big % i == 0 and small % i == 0:
            return i
    return None


def greatest_common_divisor1(x, y):             # 辗转相除法
    big = max(x, y)
    small = min(x, y)
    if big % small == 0:
        return small
    return greatest_common_divisor1(small, big % small)


def greatest_common_divisor2(x, y):             # 更相减损法
    a = max(x, y)
    b = min(x, y)
    if a - b == b:
        return b
    c = a - b
    return greatest_common_divisor2(b, c)


print(greatest_common_divisor2(20, 10))
