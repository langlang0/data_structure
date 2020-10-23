def partition(nums, start, end) -> int:
    target = nums[start]
    i = start + 1
    j = end
    while i <= j:
        while i <= j and nums[i] < target:
            i += 1
        while i <= j and nums[j] >= target:
            j -= 1
        if i < j:
            nums[i],nums[j] = nums[j],nums[i]
    nums[start],nums[j] = nums[j],nums[start]
    return j


def partition1(nums,start,end) -> int:
    target = nums[start]
    j = start
    for i in range(start + 1, end + 1):
        if nums[i] < target:
            j += 1
            nums[i],nums[j] = nums[j],nums[i]
    nums[start],nums[j] = nums[j],nums[start]
    return j


def quicksort(nums,start,end):
    if start >= end:
        return nums
    mind = partition(nums,start,end)
    quicksort(nums,start,mind - 1)
    quicksort(nums,mind + 1,end)


if __name__ == '__main__':
    a = [2, 5, 9, 4, 7, 3, 1, 0]
    quicksort(a,0,7)
    print(a)
