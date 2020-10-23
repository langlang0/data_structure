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


def mergeSort(nums:List):
    if len(nums) <= 1:
        return nums
    middle = len(nums) >> 1
    left, right = nums[:middle], nums[middle:]
    return merge(mergeSort(left),mergeSort(right))


if __name__ == '__main__':
    a = [1,4,7,2,5,9,3,8]
    print(mergeSort(a))