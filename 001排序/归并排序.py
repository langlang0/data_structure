from typing import List


def mergeSort(iList: List):  # 分组
    if len(iList) <= 1:
        return iList
    middle = len(iList) >> 1
    left, right = iList[:middle], iList[middle:]
    return merges(mergeSort(left), mergeSort(right))


def merge(left, right):                     # 列表append和pop
    mList = []
    while left and right:
        if left[0] < right[0]:
            mList.append(left.pop(0))
        else:
            mList.append(right.pop(0))
    if left:
        mList.extend(left)
    if right:
        mList.extend(right)
    return mList


def merges(left, right):                 # 指针法
    res = []
    poin1 = 0
    poin2 = 0
    while poin1 < len(left) and poin2 < len(right):
        if left[poin1] < right[poin2]:
            res.append(left[poin1])
            poin1 += 1
        else:
            res.append(right[poin2])
            poin2 += 1
    res.extend(left[poin1:])
    res.extend(right[poin2:])
    return res


if __name__ == '__main__':
    a = [3, 4, 6, 2, 7, 9, 1]
    print(merdeSort(a))
