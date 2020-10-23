def move(lists: list, a: int):
    slow = 0
    fast = 0
    while fast < len(lists):
        if lists[fast] == a:
            fast += 1
        else:
            lists[slow] = lists[fast]
            slow += 1
            fast += 1
    return lists[:slow]


def twosum(lists: list, a: int):
    left = 0
    right = len(lists) - 1
    res = []
    while left < right:
        if lists[left] + lists[right] < a:
            left += 1
        elif lists[left] + lists[right] > a:
            right -= 1
        else:
            res.append([lists[left], lists[right]])
            left += 1
            right -= 1
    return res


if __name__ == '__main__':
    print(move([1, 2, 4, 6, 21, 1], 1))
    print(twosum([2, 3, 5, 7, 8, 9], 11))
