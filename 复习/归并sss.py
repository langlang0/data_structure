from typing import List


def merge(left, right):
    res = []
    while left and right:
        if left[0] < right[0]:
            res.append(left.pop(0))
        else:
            res.append(right.pop(0))
    if left:
        res += left
    if right:
        res += right
    return res


def merges(left, right):
    res = []
    l = 0
    r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res += [left[l]]
            l += 1
        else:
            res += [right[r]]
            r += 1
    if l < len(left):
        res += left[l:]
    if r < len(right):
        res += right[r:]
    return res


def mergeSort(nums: List):
    if len(nums) <= 1:
        return nums
    midden = len(nums) >> 1
    left, right = nums[:midden], nums[midden:]
    return merges(mergeSort(left), mergeSort(right))


def swap(nums, p, q):
    nums[p],nums[q] = nums[q],nums[p]


def partition(nums, start, end) -> int:
    pivot = nums[start]
    p = start + 1
    q = end
    while p <= q:
        while p <= q and nums[p] < pivot:
            p += 1
        while p <= q and nums[q] >= pivot:
            q -= 1
        if p < q:
            swap(nums,p,q)
    swap(nums,start,q)
    return q




def quickSort(nums: List, start, end):
    if start >= end:
        return nums
    mid = partition(nums, start, end)
    quickSort(nums,start,mid - 1)
    quickSort(nums,mid + 1,end)


if __name__ == '__main__':
    a = [2, 5, 9, 4, 7, 3, 1, 0]
    print(mergeSort(a))
