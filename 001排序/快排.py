from typing import List


def swap(iList, p, q):
    iList[p], iList[q] = iList[q], iList[p]


def partition(iList, start, end) -> int:  # 双指针排序
    pivot = iList[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and iList[p] < pivot:
            p += 1
        while p <= q and iList[q] >= pivot:
            q -= 1
        if p < q:
            swap(iList, p, q)
    swap(iList, start, q)
    return q


def partition1(array,start,end):            # 单指针排序
    pivot = array[start]
    mark = start
    for i in range(start + 1, end + 1):
        if array[i] < pivot:
            mark += 1
            array[mark], array[i] = array[i], array[mark]
    array[start],array[mark] = array[mark],array[start]
    return mark


def quickSort(iList, start, end):   # 分组
    if start >= end:
        return
    mid = partition1(iList, start, end)
    quickSort(iList, start, mid - 1)
    quickSort(iList, mid + 1, end)


if __name__ == '__main__':
    a = [2, 5, 9, 4, 7, 3, 1, 0]
    quickSort(a,0,7)
    print(a)